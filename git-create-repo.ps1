$workdir =  Convert-Path $pwd

$gituser = "l00tz1ffer"
$gitserver = "lootziffers-welt.de"

$workDirName = $workdir.Substring(($workdir.LastIndexOf("\") + 1), ($workdir.Length -1 ) - $workdir.LastIndexOf("\"))

$git_dir_string = $workDirName + ".git"

"git-create-repo.ps1" >> $workdir/.gitignore

ssh git@$gitserver "cd  $gituser && mkdir $git_dir_string && cd $git_dir_string && git init --bare"



git init
echo "Lokales Repo wurde Initialisiert"




git add .
echo "Dateien wurden zum Lokalen Repository hinzugef�gt"

git commit -m "initialisierendes Commit"
echo "Initialisierender Commit Ausgef�hrt"


$git_repo_string = "git@lootziffers-welt.de:"+$gituser+"/" + $workDirName + ".git"
echo "Der Verwendete Remote Git Repo string lautet: " + $git_repo_string

git remote add origin $git_repo_string
git push origin master

Start-Sleep -Seconds 5