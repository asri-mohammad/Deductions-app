# Deductions-app

The app consists of 3 sections, including:
1. main section 
2. retires util section 
3. back up section

Let us describe what each section's parts are and what they do.

## 1. main
* **Info :** This tab allows users to search for a borrower to view their personal information, access a detailed report on their monthly payments, and change the borrower's general status.
* **Monthly calculation :**  This is where the current month's calculation takes place, including updating borrowers' work statuses, generating bank-related documents, and creating next month's deductions lists based on provided responses.
* **Monthly data :** Allows the user to store monthly inputs and outputs for future reference, providing access to a report on each month's operations at any point in time. Furthermore, it updates borrowers' loan residue according to the given lists.
* **Batch operation :** A place for actions that may be needed to be done in bulk for a set of borrowers.
* **Insurance setting :**  Lets the user control the list of those eligible for an insurance claim and the reasoning behind it, affecting the monthly list sent to the insurance company.
## 2. retires
* **Response division :** This part involves preprocessing raw retires monthly response list based on some predefined criteria.
* **Request list :**  It generates the final retires request list from multiple lists.

## 3. backup
Makes it available for the user to regularly backup the database and, in case of corruption, restore the application data from a backup file.
