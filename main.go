package main

import(
  "flag"
  "fmt"
  "github.com/bwmarrin/discordgo"
  "os"
  "os/signal"
)

var(
  guildID = flag.String("guild", "919846932459974686", "Specifies the guild to work for.")
  removeCMD = flag.Bool("rmvcmd", true, "Removes commands on shutdown.")
  token = flag.String("token", os.Getenv("CLIENT_TOKEN"), "Access token.")
)

var(
  commands = []*discordgo.ApplicationCommand {
    //impl
  }
  
  commandHandler = map[string] func(s *discordgo.Session, i *discordgo.InteractionCreate) {
    //impl
  }
)

func main() {
  client, err := discordgo.New("Bot" + *token)
  client.Identify.Intents = discordgo.IntentsAll
  
  status := discordgo.UpdateStatusData {
    Activities: []*discordgo.Activity {
      {
        Name: " myself grow."
        Type: 3,
      },
    },
  }
  
  // Error check if the client cannot create the session
  if err != nil {
    fmt.Println("There was an error creating session: ", err)
  }
  
  // Error check if the client does not open the connection
  err = client.Open()
  if err != nil {
    fmt.Println("There was an error opening the connection: ", err)
  }
  
  // Event handler that deals with the command handling and update the status
  client.UpdateStatusComplex(status)
  
  client.AddHandler(func(s *discordgo.Session, i *discordgo.InteractionCreate) {
    if handler, ok := commandHandler[i.ApplicationCommandData().Name]; ok {
      handler(s, i)
    }
  })
  
  // This part handles the creation of the slash commands
  registerCommands := make([]*discordgo.ApplicationCommand, len(commands))
  
  for ctr, v := commands {
    command, err := client.ApplicationCommandCreate(client.State.User.ID, *guildID, v)
    
    // Error check if the command could not be created
    if err != nil {
      fmt.Printf("Error occurred during the creation of %v command: %v", v.Name, err)
    }
    
    registerCommands[ctr] = command
  }
  
  // A simple stopping measure to shutdown the client
  defer client.Close()
  
  halt := make(chan os.Signal, 1)
  signal.Notify(halt, os.Interrupt)
  <- halt
  
  // This handles the removal of the commands upon shutting down the client
  if *removeCMD {
    for _, v := range registerCommands {
      err := client.ApplicationCommandDelete(client.State.User.ID, *guildID, v)
      
      // Error check if the commands cannot be deleted
      if err != nil {
        fmt.Printf("Error occurred during deletion of %v command: %v", v.Name, err)
      }
    }
  }
  
}
