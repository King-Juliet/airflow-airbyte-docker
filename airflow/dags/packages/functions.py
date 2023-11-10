#IMPORT LIBRARIES
import pandas as pd
import numpy as np
import requests
import psycopg2
from google.cloud import storage
import gcsfs


#Custom functions
#Extract from API to GCS functions

def get_and_extract_fakestore_product_to_gcs(destination_gcs_path, url="https://fakestoreapi.com/products"):
    response = requests.get(url)

    if response.status_code == 200:
        products = response.json()

        if products:
            data = []
            for product in products:
                # Extract information from each product
                product_id = product.get("id")
                product_name = product.get("title")
                product_price = product.get("price")

                # Append the extracted information to the data list
                data.append({"Product_ID": product_id, "Name": product_name, "Price": product_price})

            # Create a DataFrame from the list of dictionaries
            df = pd.DataFrame(data)
            #load data to gcs
            fs = gcsfs.GCSFileSystem(project='merch-store-399816')
            with fs.open(destination_gcs_path, 'wb') as f:
                 #df.to_parquet(f, index=False)
                 df.to_csv(f, index=False)
        else:
            print("No data available")
            return None
    else:
        print(f"Error: {response.status_code}")
        return None

# Example usage
#fakestore_product_data_df = get_and_extract_fakestore_data()
#print(fakestore_product_data_df)

def get_and_extract_fakestore_cart_to_gcs(destination_gcs_path, url="https://fakestoreapi.com/carts"):
    response = requests.get(url)

    if response.status_code == 200:
        cart_items = response.json()

        if cart_items:
            data = []
            for cart in cart_items:
                cart_id = cart.get("id")
                user_id = cart.get("userId")
                date = cart.get("date")

                # Extract product details from the cart items
                for item in cart.get("products", []):
                    product_id = item.get("productId")
                    product_name = item.get("title")
                    product_price = item.get("price")
                    quantity = item.get("quantity")

                    data.append({
                        "Cart_ID": cart_id,
                        "User_ID": user_id,
                        "Date": date,
                        "Product_ID": product_id,
                        "Product_Name": product_name,
                        "Product_Price": product_price,
                        "Quantity": quantity
                    })

            # Create a DataFrame from the list of dictionaries
            df = pd.DataFrame(data)
            #load data to gcs
            fs = gcsfs.GCSFileSystem(project='merch-store-399816')
            with fs.open(destination_gcs_path, 'wb') as f:
                 #df.to_parquet(f, index=False)
                 df.to_csv(f, index=False)
        else:
            print("No cart data available")
            return None
    else:
        print(f"Error: {response.status_code}")
        return None

# Example usage
#fakestore_cart_data_df = get_and_extract_fakestore_cart_data()
#print(fakestore_cart_data_df)

def get_and_extract_fakestore_users_to_gcs(destination_gcs_path, url="https://fakestoreapi.com/users", ):
    response = requests.get(url)

    if response.status_code == 200:
        users_data = response.json()

        if users_data:
            data = []
            for user in users_data:
                data.append({
                    "User_ID": user.get("id"),
                    "Username": user.get("username"),
                    "Password": user.get("password"),
                    "Email": user.get("email"),
                    "Phone_number": user.get("phone"),
                    "Firstname": user.get("name", {}).get("firstname"),
                    "Lastname": user.get("name", {}).get("lastname"),
                    "City": user.get("address", {}).get("city"),
                    "Street": user.get("address", {}).get("street"),
                    "Number": user.get("address", {}).get("number"),
                    "Zipcode": user.get("address", {}).get("zipcode"),
                    "Latitude": user.get("address", {}).get("geolocation", {}).get("lat"),
                    "Longitude": user.get("address", {}).get("geolocation", {}).get("long")
                })

            # Create a Pandas DataFrame from the list of dictionaries
            df = pd.DataFrame(data)
            #load data to gcs
            fs = gcsfs.GCSFileSystem(project='merch-store-399816')
            with fs.open(destination_gcs_path, 'wb') as f:
                 #df.to_parquet(f, index=False)
                 df.to_csv(f, index=False)
        else:
            print("No user data available")
            return None
    else:
        print(f"Error: {response.status_code}")
        return None

# Example usage
#fakestore_users_data_df = get_and_extract_fakestore_users_data()
#print(fakestore_users_data_df)
