from requests_html import HTMLSession
import csv

session = HTMLSession()
product_id = 1

with open("Jumia_product.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["id", "page number", "product name", "price",
                    "reviews", "avg_rate", "brand", "desc", "image"])
    for x in range(1, 50):
        page = session.get(
            f"https://www.jumia.com.eg/ar/all-products/?page{x}#catalog-listing")
        all_products = page.html.xpath(
            "/html/body/div[1]/main/div[2]/div[3]/section/div[1]", first=True)

        print(f"page number {x}....")

        for product in all_products.absolute_links:
            product_page = session.get(product)

            try:
                product_name = product_page.html.find(
                    "h1.-pbxs", first=True).text
            except:
                product_name = ""
            try:
                product_price = product_page.html.find(
                    "span.-fs24", first=True).text
            except:
                product_price = ""
            try:
                product_reviews = product_page.html.find(
                    "p.-pts", first=True).text
            except:
                product_reviews = ""
            try:
                product_avg_rate = product_page.html.find(
                    "span.-b", first=True).text
            except:
                product_avg_rate = ""
            try:
                product_brand_selector = '#jm > main > div:nth-child(1) > section > div > div.col10 > div.-phs > div:nth-child(1) > a:nth-child(1)'
                product_brand = product_page.html.find(
                    product_brand_selector, first=True).text
            except:
                product_brand = ""
            try:
                product_desc = product_page.html.find(
                    "div.markup.-mhm.-pvl.-oxa.-sc", first=True).text
            except:
                product_desc = ""
            try:
                product_image = product_page.html.find(
                    "#imgs > a:nth-child(2) > img", first=True).attrs["data-src"]
            except:
                product_image = ""

            writer.writerow([product_id, x, product_name,
                            product_price,
                            product_reviews,
                            product_avg_rate,
                            product_brand,
                            product_desc,
                            product_image])
            product_id += 1


        print(f"----------- end page number {x} ------------------")
