# Python-Markdown-Converter-Tool
This is the tool I use to convert the Markdown files of my blog posts to HTML and Json. To run this app you will need another filed called GitIgnore.py which will contain the file locations for the private version and public version of your target locations:
private_md_path
private_json_path
private_html_path 
public_json_path 
public_html_path 
After that you should be able to run this without issue. It takes in the files from the private_md_path and takes out the YAML code at the top then it converts the text using a template you provide it with private_html_path. 