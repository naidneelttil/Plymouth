// Require the necessary discord.js classes
const { Client, Events, GatewayIntentBits } = require('discord.js');
const { token } = require('./config.json');

// Create a new client instance
const client = new Client({ intents: [GatewayIntentBits.Guilds] });

// When the client is ready, run this code (only once).
// The distinction between `client: Client<boolean>` and `readyClient: Client<true>` is important for TypeScript developers.
// It makes some properties non-nullable.
client.once(Events.ClientReady, (readyClient) => {
	console.log(`Ready! Logged in as ${readyClient.user.tag}`);
});

// Log in to Discord with your client's token
client.login(token);


client.on('messageCreate', message => {
	if (message.content === '?role') {
		// if you are an admin or a chat mod, you should be able to change roles
		const modRole = message.guild.roles.cache.find(role => role.name === 'Administrator' || role.name === 'Chat Moderator');
		if (message.member.roles.cache.has(modRole.id)) {
			message.reply('You have access to this command!');
			// Place role command actions here
		}
		else {
			message.reply('Only moderators can use this command.');
		}
	}
});
