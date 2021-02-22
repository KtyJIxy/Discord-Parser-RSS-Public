# Discord Parser RSS Bot

Discord Parser RSS is a simple Discord bot built on Python that does two things:
- Brings your RSS subscriptions for last 24 hours on command;
- Parses web-sites and prints text directly into channel.

## Getting it started:
1. Clone this repository and **keep it private**.
2. At [Discord Developer Portal](https://discord.com/developers/applications) create new application. Remember `Client ID`.
3. At application page on Discord Developer Portal create a bot and save token (**KEEP IT SECRET**.)
4. Create a Discord Server or be sure to have bot-inviting rights on existing one.
5. Invite your bot to server by link: https://discord.com/oauth2/authorize?client_id=`Client ID numbers`&scope=bot.
6. Get back to GitHub and save your token in code, 11th line. *Alternatively, there are ways to load your token into file. Discussed below.*
7. Create a [Heroku](https://dashboard.heroku.com/) account.
8. Create a new App with unique name. On `Settings` page in `Buildpack` choose Python.
9. On `Deploy` page link your Heroku account to Github account, choose your Discord Parser RSS Bot repository and deploy it.
10. On `Resources` page activate worker.
11. Test your bot. It should work now, except `?rss_daily` command.
12. In `FEED_URL` (line 32) add all your XML RSS subscriptions, push and re-deploy. All set.

### Loading token into file
You either can set up an .env at Heroku ([check manual](https://devcenter.heroku.com/articles/config-vars)) or load it locally, through a `JSON-mapping`, for example. Latter will require installing of [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli) and, **of course** addition of according `.gitignore` line. You will stage your bot directly from your local repository, so you won't need a GitHub linking to Heroku anymore.

### Things to consider while using:
- Parse function prints all the text on page, ***despite how page long is***. If you're using it for same sites, you may want to make it parse through specific block-codes on page. Of course, every site has different HTML structure, so you will have to write code for every situation.
- If you're setting bot not only for yourself, but for a community, you may want to add user commands to add to FEED_URL.
- RSS function is set to bring links of content. If your subscription is, for example, photos, you'll have to change parsed [XML-structure](https://www.w3schools.com/xml/xml_rss.asp) accordingly.