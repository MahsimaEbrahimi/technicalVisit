import webbrowser
import os

def Create_html(blueprintPath, outputPath, date, carId, shasiNumber, carType, color, name, motorInput, 
                girboxInput, blockingAndSuspentionInput, options, explaination):
    html_content = ''
    with open(blueprintPath, 'r', encoding='utf-8') as file:
        html_content = file.read()

    html_content = html_content.replace("{{date}}", date)
    html_content = html_content.replace("{{carid}}", carId)
    html_content = html_content.replace("{{shasinumber}}", shasiNumber)
    html_content = html_content.replace("{{cartype}}", carType)
    html_content = html_content.replace("{{color}}", color)
    html_content = html_content.replace("{{name}}", name)
    html_content = html_content.replace("{{motorInput}}", motorInput)
    html_content = html_content.replace("{{girboxInput}}", girboxInput)
    html_content = html_content.replace("{{blockingAndSuspentionInput}}", blockingAndSuspentionInput)
    html_content = html_content.replace("{{options}}", options)
    html_content = html_content.replace("{{explaination}}", explaination)

    with open(outputPath, 'w', encoding='utf-8') as file:
        file.write(html_content)

def Show_in_browser(path):
    webbrowser.open(f"file://{os.path.abspath(path)}")

def Delete_html(path):
    if os.path.exists(path):
        os.remove(path)