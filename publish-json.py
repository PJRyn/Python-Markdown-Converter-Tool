import json
import yaml
import os
from os import listdir
from os.path import join, isfile
import markdown
import re
import gitignore as gi

#get json into output_path
def get_metadata(path, output_path) :
    posts_metadata = []
    for filename in listdir(path):  # iterates over all the files in 'path'
        full_path = join(path, filename)  # joins the path with the filename
        if isfile(full_path):  # validate that it is a file
            with open(full_path) as f:  # open the file
                post_metadata = next(yaml.load_all(f, Loader=yaml.FullLoader)) # extract yaml metadata
                posts_metadata.append(post_metadata) # add to list
    # Output the list as a json file, currently named testing.
    output = join(output_path, "index.json")
    with open(output, "w") as outfile:
        json.dump(posts_metadata, outfile,indent=1,sort_keys=True)

#Cleans old posts out
def clearn_HTML(target_path) :
    for filename in listdir(target_path) : #iterates through all files in 'path'
        file_path = os.path.join(target_path, filename)
        os.remove(file_path)

#set output
def get_HTML(path, output_path) :
    for filename in listdir(path):  # iterates over all the files in 'path'
        output_filename = filename.replace(".md", ".html") #output files as .html not .md

        full_path = join(path, filename)  # joins the path with the filename
        output = join(output_path, output_filename) #joins output path with filename
        output = output.replace(" ", "_")
        if isfile(full_path):  # validate that it is a file
            with open(full_path) as f:  # open the file
                markdown.markdownFromFile(input= full_path, output= output, encoding='utf8')

#get htmls to output path
def format_HTML(path, output_path) :
    for filename in listdir(path):  # iterates over all the files in 'path'
        full_path = join(path, filename)  # joins the path with the filename
        if isfile(full_path):  # validate that it is a file
            with open(full_path, "r") as f:  # open the file
                templateHTML = open("../template/template.html", "r") # open template file
                template = templateHTML.read() # read template file
                insert = f.read() # read the current html
                output_html_formatted = template.replace("insert_post", insert) # insert posts into the template
                output_html_formatted = re.sub('<hr />.*?<hr />', '', output_html_formatted, flags=re.DOTALL) # remove the metadata yaml
                with open(full_path, "w") as file:
                    file.write(output_html_formatted) # replace html files with cleaned and templated versions

def menu() :
    print("+===========+")
    print("Hello User: " +
          "\n 1-Publish Private" + "\n 2-Publish to Public" +"\n 3-Full publish" + "\n 4-Quit")
    user_select = input("Select: ")
    match user_select:
        case "1":
            print("Publishing to Private")
            get_metadata(gi.private_md_path,gi.private_json_path)
            clearn_HTML(gi.private_html_path)
            get_HTML(gi.private_md_path,gi.private_html_path)
            format_HTML(gi.private_html_path,gi.private_html_path)

        case "2":
            print("Publishing to pbulic")
            get_metadata(gi.private_md_path,gi.public_json_path)
            clearn_HTML(gi.public_html_path)
            get_HTML(gi.private_md_path,gi.public_html_path)
            format_HTML(gi.public_html_path,gi.public_html_path)
        case "3":
            print("Publishing to both")
            print("Publishing to Private")
            get_metadata(gi.private_md_path,gi.private_json_path)
            clearn_HTML(gi.private_html_path)
            get_HTML(gi.private_md_path,gi.private_html_path)
            format_HTML(gi.private_html_path,gi.private_html_path)
            get_metadata(gi.private_md_path,gi.public_json_path)
            clearn_HTML(gi.public_html_path)
            get_HTML(gi.private_md_path,gi.public_html_path)
            format_HTML(gi.public_html_path,gi.public_html_path)
        case "4":
            quit()
        case _:
            print("invalid input, try 1 - 4")

menu()