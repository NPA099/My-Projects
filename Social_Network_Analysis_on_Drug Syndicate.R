library(shiny)
library(reshape)
library(dplyr)
library(networkD3)
library(igraph)
library(data.table)
library(sqldf)
library(shinythemes)

#shinyUI(fluidPage(
ui <- fluidPage(#theme = shinytheme("superhero"), 
  shinythemes::themeSelector(), 
  
  titlePanel("Narayanan_Padmanabhan_SNA"),
  #sidebarLayout(
  #sidebarPanel(
  
  #fileInput("file","Choose the file", accept = c(
   # "text/csv",
    #"text/comma-separated-values,text/plain",
    #".csv"))
  
  #),
  mainPanel(
    tabsetPanel(
      tabPanel('Summary', 'Total number of calls:', textOutput('total_calls'), 
               'Most calls were received by: ', tableOutput('Received_Calls'), 
               'Most calls were placed by: ', tableOutput('Placed_Calls')), 
      tabPanel('Source_Table', tableOutput('src_data')),
      tabPanel('Long_Table', tableOutput('src_data_long')), 
      tabPanel('Filtered_Long_Table', tableOutput('src_data_long_filtered')),
      tabPanel('Centrality', tableOutput('centrality')),
      
      tabPanel('Undirected_Network', 
               'The size of the nodes corresponds to the degree centrality', 
               forceNetworkOutput('undir_graph_d3_forced')),
      tabPanel('Directed_Network_Inbound', 
               'The size of the nodes corresponds to the indegree centrality', 
               forceNetworkOutput('dir_graph_d3_forced_inbound')),
      tabPanel('Directed_Network_Outbound', 
               'The size of the nodes corresponds to the outdegree centrality', 
               forceNetworkOutput('dir_graph_d3_forced_outbound')), 
      tabPanel('Observations', 'Following are the observations from the 3 networks:', 
               
               '1. Kay is the most influential person in the network, this is evident from the 
               high degree centrality (24) and betweenness centrality (311.5).', 
               '2. We can see a hierarchial pattern in this drug dealing network, Kay being the 
               central point of contact.', 
               '3. People like Dante, Manna, Tommy and Steve are also influential people in the 
               network.', 
               '4. Higher betweenness for Tommy (31), Steve (26.5), and Dante (26), show that they 
               are the backbones of this network. Without them, people in the tail of the network 
               cannot be contacted.')
      
      
      #tabPanel('Undirected_Network', simpleNetworkOutput('undir_graph_d3'), width = "100%", height = "500px"),
      #tabPanel('Directed_Network', plotOutput('dir_graph_i'))
      
      #tabPanel('Summary'), h1('Number of calls placed: '), verbatimTextOutput('total_calls')
      #)
      #uiOutput("fieldf")
      
      )
    
    
    )
  
  
)


#shinyServer(function(input,output){
server <- function(input,output){

  data1 <- read.csv('COCAINE_DEALING.csv')
  colnames(data1)[1] <- "Calling_Party"
  data2 <- melt.data.frame(data1, id.vars = "Calling_Party")
  colnames(data2)[2] <- "Called_Party"
  output$src_data <- renderTable({data1})
  output$src_data_long <- renderTable({data2})
  
  #Filtering the rows where there was a communication
  data3 <- data2[data2$value != 0,]
  output$src_data_long_filtered <- renderTable({data3})
  
  #aggregate(data3$value, fun = sum)
  #Total number of calls that were placed
  #total_calls <- sum(data3$value)
  #output$total_calls <- renderPrint({total_calls()})
  output$total_calls <- renderText({sum(data3$value)})
  
  #Received calls
  data4 <- aggregate(value~Called_Party, data3, FUN = sum)
  
  #Identifying the person who received the most number of calls
  data5 <- data4%>%
    select(Called_Party, value)%>%
    filter(value == max(value))
  
  output$Received_Calls <- renderTable({data5})
  
  #Placed calls
  data6 <- aggregate(value~Calling_Party, data3, FUN = sum)
  
  #Identifying the person who placed the most number of calls
  data7 <- data6%>%
    select(Calling_Party, value)%>%
    filter(value == max(value))
  
  output$Placed_Calls <- renderTable({data7})
  
  #Simple network model undirected
  output$undir_graph_d3 <- renderSimpleNetwork({
    simpleNetwork(data3, Source = 1, Target = 2, nodeColour = "green", fontSize = 16, 
                  linkColour = "grey", zoom = T)
  }) 
  
  
  
  #Network model undirected
  undir_graph <- graph.data.frame(data3[,1:2], directed = F) 
  
  #Network model directed
  dir_graph <- graph.data.frame(data3[,1:2], directed = T) 
  
  #output$dir_graph_i <- renderPlot({
  #plot.igraph(dir_graph, arrow.width = 0.01, loop.angle2 = 1)
  #tkplot(dir_graph, vertex.colour = 'green')
  #plot(dir_graph)
  #})
  
  #Degree and betweenness centrality
  deg_undir <- as.data.frame(degree(undir_graph))
  bet_undir <- as.data.frame(betweenness(undir_graph))
  deg_dir_in <- as.data.frame(degree(dir_graph, mode = 'in'))
  deg_dir_out <- as.data.frame(degree(dir_graph, mode = 'out'))
  #Converting rownames to first column
  setDT(deg_undir, keep.rownames = T)[]
  setDT(deg_dir_in, keep.rownames = T)[]
  setDT(deg_dir_out, keep.rownames = T)[]
  setDT(bet_undir, keep.rownames = T)[]
  centrality_measure <- merge.data.frame(deg_undir,deg_dir_in, by.x = 'rn', by.y = 'rn')
  centrality_measure <- merge.data.frame(centrality_measure,deg_dir_out, by.x = 'rn', by.y = 'rn') 
  centrality_measure <- merge.data.frame(centrality_measure,bet_undir, by.x = 'rn', by.y = 'rn')
  colnames(centrality_measure)[1] <- "party_name"
  colnames(centrality_measure)[2] <- "deg_undir"
  colnames(centrality_measure)[3] <- "deg_dir_in"
  colnames(centrality_measure)[4] <- "deg_dir_out"
  colnames(centrality_measure)[5] <- "bet_undir"
  output$centrality <- renderTable({centrality_measure})
  
  
  
  #Pre-processing data for forced network
  #Generating Nodes data frame
  df_nodes <- data.frame(Nodes = union(data3$Calling_Party, data3$Called_Party))
  setDT(df_nodes, keep.rownames = T)
  #Converting the row number to numeric to generate node id
  df_nodes <- transform(df_nodes, rn = as.numeric(rn))
  df_nodes <- transform(df_nodes, Node_ID = rn - 1)
  #Generating the links data frame
  df_links <- sqldf('select Calling_Party, Called_Party, value, df_nodes.Node_ID as Source 
                    from data3 join df_nodes on data3.Calling_Party = df_nodes.Nodes')
  df_links <- sqldf('select Calling_Party, Called_Party, value, Source, df_nodes.Node_ID as Target 
                    from df_links join df_nodes on df_links.Called_Party = df_nodes.Nodes')
  
  #Including centrality measures for determining the size of the nodes in the forced network models
  df_nodes_undir <- sqldf('select Nodes, Node_ID, deg_undir 
                          from df_nodes join centrality_measure on df_nodes.Nodes = centrality_measure.party_name')
  
  df_nodes_dir_in <- sqldf('select Nodes, Node_ID, deg_dir_in 
                           from df_nodes join centrality_measure on df_nodes.Nodes = centrality_measure.party_name')
  
  df_nodes_dir_out <- sqldf('select Nodes, Node_ID, deg_dir_out 
                            from df_nodes join centrality_measure on df_nodes.Nodes = centrality_measure.party_name')
  
  #Undirected forced network plot
  output$undir_graph_d3_forced <- renderForceNetwork({
    forceNetwork(Links = df_links, Nodes = df_nodes_undir, Source = 'Source', Target = 'Target', Value = 'value', 
                 NodeID = 'Nodes', Group = 'Node_ID', zoom = T, arrows = F, opacity = 0.9,  
                 radiusCalculation = 'Math.sqrt(d.nodesize)+6', Nodesize = 'deg_undir')
  })
  
  #Directed forced network plot inbound
  output$dir_graph_d3_forced_inbound <- renderForceNetwork({
    forceNetwork(Links = df_links, Nodes = df_nodes_dir_in, Source = 'Source', Target = 'Target', Value = 'value', 
                 NodeID = 'Nodes', Group = 'Node_ID', zoom = T, arrows = T, opacity = 0.9,  
                 radiusCalculation = 'Math.sqrt(d.nodesize)+6', Nodesize = 'deg_dir_in')
  })
  
  #Directed forced network plot Outbound
  output$dir_graph_d3_forced_outbound <- renderForceNetwork({
    forceNetwork(Links = df_links, Nodes = df_nodes_dir_out, Source = 'Source', Target = 'Target', Value = 'value', 
                 NodeID = 'Nodes', Group = 'Node_ID', zoom = T, arrows = T, opacity = 0.9,  
                 radiusCalculation = 'Math.sqrt(d.nodesize)+6', Nodesize = 'deg_dir_out')
  })
  
  
}


shinyApp(ui = ui,server = server)