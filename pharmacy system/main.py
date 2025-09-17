from pharmasi import *


def main():
    opharmacy = pharmasi()
    while True:
        client_or_supplier = input("Clinet or Supplier: ").strip().lower()
        if client_or_supplier == "supplier":
            opharmacy.supplier()
        elif client_or_supplier == "client":
            opharmacy.clinet()


if __name__ == "__main__":
    main()
