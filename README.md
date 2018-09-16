# One Minute Pitch
>The One-minute-pitch is a Flask based application that allows users to present their pitches on the site in order to market themselves.The One-minute-Pitch allows users to create an account and login and make a pitch,upvote or downvote a pitch etc

[Live Link](https://dbminutepitch.herokuapp.com/)

This website will allow you to submit your pitches and other users will vote on them and leave comments to give their feedback on them.


## As users you can

* submit a pitch in any category.
* see the pitches other people have posted.
* favourite other people's posts
* vote on the pitch they liked by giving it a downvote or upvote.
* comment on the different pitches.
* view the different categories.

## Usage example

To create an account access the live link.

Click on register and fill in your details
on the form shown.

Now you can login with the new credentials.

On login, you can view posts from other users
You can like, comment and favourite them.

When, you favourite them, They are saved to your
favourites tab and you can access them quickly on login.

After posting a pitch or a comment, you can review them,
on then my account section. Here, you can delete your comments
or posts if your not satisfied by them.


## Development setup

To access the Code behind this site, you will need to:

1. Clone this repo:
  ```bash
  git clone 
  ```
2. Move to the folder and install requirements
  ```bash
  cd One-minute-pitch
  pip install -r requirements.txt
  ```
3. Export Configurations to environment
  ```bash
  export SECRET_KEY='{Your Secret Key}'
  export DATABASE_URL='postgresql+psycopg2://{Your username}:{password}@localhost/{Your database name}'
  ```
4. Run the application
  ```bash
  python3.6 manage.py server


## Technologies Used


* python3
* Flask
* Jinja templates
* HTML
* Bootstrap
* Bootswatch


### License


Copyright (c) [Evoh Mike](https://github.com/Evohmike/One-Minute-Pitch/blob/master/LICENSE)
git 
