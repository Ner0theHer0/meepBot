# meepBot
Basic discord bot allowing for adminless role management with a hard whitelist

This is a privately hosted bot, and cannot be simply added to a server like publicly hosted one. You will have to create a discord dev account 
if you don't already have one, create a bot and run it (i.e. host it) using the code in this repository.

NOTE: This repository does not contain the required token for your bot within the .env file. You will have to update this file with the private
token that you receive when you create the bot. It should look as follows:

`DISCORD_TOKEN=(your token here)`

This file will have the be renamed `.env` via the command line to work properly - it is held as envTemplate in the repo.

Currently, there are some issues with a microsoft certificate and hosting bots on windows machines. The fix can be found [here](https://github.com/Rapptz/discord.py/issues/4159).

## Role Management

### Admin Tools
* !whitelist (role): Adds a role to whitelist if such a role exists in the server, and is not already in the whitelist. If the role is already in the whitelist, it removes it.
* !exit: Shuts the bot down (helpful if you are running this service from a hidden shell)
	
### User Commands 
* !role: Lists the available self-assignable roles to the user
* !role (roleName): If the user does not have this role and it self-assignable, they are assigned the role. If they already have the role, it is removed from them.
* !whitelist: Lists the available self-assignable roles to the user

### Misc Commands
These commands are a good example of things that can be impletemented on top of this role management platform. Tailor these to your liking.
* !dota: Pings all users with the @dota role with a custom message
* !kalpa: Pings a special user and appends a random special message
* !git: Posts the github link to this bot
