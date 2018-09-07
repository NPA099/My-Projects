library(shiny)
library(tm)
library(wordcloud)
library(data.table)
library(sqldf)
library(tidytext)
library(dplyr)
library(ggplot2)
library(stringr)

ui <- fluidPage(
  titlePanel("Narayanan_Padmanabhan_NLP"),
  #sidebarLayout(
  #sidebarPanel()
  #),
  
  mainPanel(
    tabsetPanel(
      tabPanel('New_Normalized_Table', tableOutput('reviews_q1')), 
      tabPanel('Term_count', tableOutput('term_cnt_txt')), 
      tabPanel('Term_count_Norm', tableOutput('term_cnt_nor_txt')), 
      tabPanel('word_cloud_1', plotOutput('word_cloud_1')), 
      tabPanel('word_cloud_2', plotOutput('word_cloud_2')),
      tabPanel('Observations_Q6', 'Following are the observations from the 2 word clouds:', 
               '1. We can see that the stop words are among the frequent terms in the original 
               text contrary to the normalized review word cloud. 
               2. The presence of these stop words in the original text can eclipse some of the 
               major sentiments and is a problem.'),
      tabPanel('Prod_Review_Score', tableOutput('prod_review_score')), 
      tabPanel('Top 6 Products', tableOutput('prod_top6')), 
      tabPanel('Scatter', plotOutput('scatter')), 
      tabPanel('Recommendations/Observations', 'From the scatter plot we can conclude that, the correlation
               is not the strong between the ratings and the sentiment scores. A bigram and 
               a trigram model could probably explain the actual sentiment of the of the reviewers in a better way. 
               We can probably improve the sentiment analysis by removing the numbers and 
               trimming the spaces, line breaks, etc from the original text.')
      
      )
      )
  
      )


server <- function(input, output){
  
  #Getting the source data 
  reviews_src <- read.csv('FewProducts.csv')
  reviews_src$Normalized_Text <- reviews_src$Text
  
  #Convert reviews to lower case
  reviews_src$Normalized_Text <- tolower(reviews_src$Normalized_Text)
  
  #Remove numbers
  reviews_src$Normalized_Text <- gsub("[[:digit:]]+", "", reviews_src$Normalized_Text)
  
  #Remove punctuations from the review text
  #reviews_src$Normalized_Text <- str_replace_all(reviews_src$Normalized_Text, pattern = "[[:punct:]]", "")
  reviews_src$Normalized_Text <- gsub("[[:punct:]]", "", reviews_src$Normalized_Text)
  #Remove extra space between the text
  reviews_src$Normalized_Text <- gsub("\\s+", " ", reviews_src$Normalized_Text)
  #Remove leading and trailing spaces
  reviews_src$Normalized_Text <- str_trim(reviews_src$Normalized_Text)
  #Remove stop words from the review text
  reviews_src$Normalized_Text <- tm::removeWords(reviews_src$Normalized_Text, stopwords(kind = 'en'))
  
  reviews_q1_df <- reviews_src[,c("Id", "ProductId", "UserId", "Text", "Normalized_Text")]
  
  #Question 1 output table: 
  output$reviews_q1 <- renderTable({reviews_q1_df})
  
  
  
  #Creating a corpus of each of the normalized review text
  #corp <- Corpus(VectorSource(reviews_src$Normalized_Text))
  
  #Creating a term document matrix of the corpus
  #tdm <- TermDocumentMatrix(corp)
  
  #Collapsing the review text to a single element
  txt_collapse <- paste(reviews_src$Text, collapse = " ")
  #Creating a corpus of the collapsed text reviews
  txt_corp <- Corpus(VectorSource(txt_collapse))
  #Creating term document matrix of the text review corpus
  tdm_txt <- TermDocumentMatrix(txt_corp)
  #Converting the term document matrix of text review as a data frame (term count table)
  tdm_txt_mat <- as.matrix(tdm_txt)
  tdm_txt_df <- as.data.frame(tdm_txt_mat)
  
  #Question 2: Term count table for the review text
  output$term_cnt_txt <- renderTable({tdm_txt_df})
  
  #Converting the row name of term count table as 1st column
  setDT(tdm_txt_df, keep.rownames = T)[]
  #Renaming the column names of the term count table
  colnames(tdm_txt_df)[1] <- "word"
  colnames(tdm_txt_df)[2] <- "frequency"
  
  #Question 3: Creating a word cloud of 200 most frequently occuring words
  ##Rendering the word cloud to shiny ui
  output$word_cloud_1 <- renderPlot(
    {
      wordcloud(tdm_txt_df$word, tdm_txt_df$frequency, max.words = 200, random.order = F, colors = brewer.pal(8, "Dark2"))
      #wordcloud(tdm_txt_df$word, tdm_txt_df$frequency, max.words = 200, random.order = F, colors = terrain.colors(length(tdm_txt_df$rn), alpha = 1))    
    }
  )
  
  
  #Collapsing the normalized review text to a single element
  norm_txt_collapse <- paste(reviews_src$Normalized_Text, collapse = " ")
  #Creating a corpus of the collapsed normalized text reviews
  norm_txt_corp <- Corpus(VectorSource(norm_txt_collapse))
  #Creating term document matrix of the normalized text review corpus
  tdm_norm_txt <- TermDocumentMatrix(norm_txt_corp)
  #Converting the term document matrix of normalized text review as a data frame (term count table)
  tdm_norm_txt_mat <- as.matrix(tdm_norm_txt)
  tdm_norm_txt_df <- as.data.frame(tdm_norm_txt_mat)
  
  #Question 4: Term count table for normalized review
  output$term_cnt_nor_txt <- renderTable({tdm_norm_txt_df})
  
  #Converting the row name of term count table as 1st column
  setDT(tdm_norm_txt_df, keep.rownames = T)[]
  #Renaming the column names of the term count table
  colnames(tdm_norm_txt_df)[1] <- "word"
  colnames(tdm_norm_txt_df)[2] <- "frequency"
  #Creating a word cloud of 200 most frequently occuring words
  ##Rendering the word cloud to shiny ui
  output$word_cloud_2 <- renderPlot(
    {
      wordcloud(tdm_norm_txt_df$word, tdm_norm_txt_df$frequency, max.words = 200, random.order = F, colors = brewer.pal(8, "Dark2"))
      #wordcloud(tdm_norm_txt_df$word, tdm_norm_txt_df$frequency, max.words = 200, random.order = F, colors = terrain.colors(length(tdm_norm_txt_df$rn), alpha = 1))    
    }
  )
  
  #Creating a replica of the normalized text variable for splitting the normalized review text
  reviews_src$words_nor <- reviews_src$Normalized_Text
  reviews_src$words_nor <- str_split(reviews_src$words_nor, " ")
  
  #Loading afinn data from afinn function in tidytext package
  afinn_tib <- get_sentiments("afinn")
  afinn_df <- as.data.frame(afinn_tib)
  
  #Function to generate the afinn score for each review text
  gen_score <- function(x){
    return(sum(afinn_df[afinn_df$word %in% x, 2]))
  }
  
  #Afinn scores corresponding to the reviews
  reviews_src$afinn_scores <- unlist(lapply(reviews_src$words_nor, gen_score))
  
  product_df1 <- aggregate(UserId~ProductId, reviews_src, FUN = length)
  product_df2 <- aggregate(afinn_scores~ProductId, reviews_src, FUN = mean)
  product_df3 <- aggregate(Score~ProductId, reviews_src, FUN = mean)
  
  product_df <- sqldf('select product_df1.ProductId, UserId as no_of_users, product_df2.afinn_scores as avg_afinn 
                      from product_df1 join product_df2 on product_df1.ProductId = product_df2.ProductId')
  
  product_df <- sqldf('select product_df.ProductId, no_of_users, avg_afinn, product_df3.Score as avg_score 
                      from product_df join product_df3 on product_df.ProductId = product_df3.ProductId')
  
  
  #Question 8: User reviews and score per product
  output$prod_review_score <- renderTable({product_df})
  
  product_top6_df <- sqldf('select ProductId from product_df order by no_of_users desc')
  
  
  product_top6_df <- head(product_top6_df, 6)
  
  #Question 9: Top 6 products
  output$prod_top6 <- renderTable({product_top6_df})
  
  #Preparing data for scatter plot
  prod_scatter_in <- reviews_src%>%
    select(ProductId, Score, afinn_scores)
  prod_scatter_in <- sqldf('select ProductId, Score, afinn_scores from prod_scatter_in where 
                           prod_scatter_in.ProductId in 
                           (select ProductId from product_top6_df)')
  
  
  scatter_in <- ggplot(prod_scatter_in, aes(x = afinn_scores, y = Score)) + geom_point() +
    geom_smooth(method = 'lm', formula = y~x)+
    facet_wrap(~ProductId)+
    xlab('Affinity Score') + ylab('Rating') +
    ggtitle('Scatter plot of the 6 most reviewed products')
  
  output$scatter <- renderPlot({scatter_in})
  
  
}


shinyApp(ui = ui,server = server)