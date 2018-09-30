#!/bin/bash

heroku login
set /p desc_commit="Descricao do Commit: "
git add .
git commit -m "%desc_commit%"
git push heroku master
heroku ps:scale web=1
heroku logs --tail
echo "Fim do Deploy"
heroku open
