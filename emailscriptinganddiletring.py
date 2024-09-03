import pandas as pd

# Load the CSV file
file_path = 'C:/Users/1234a/OneDrive/Desktop/DataScienceLearning/JupiterNotebookLearning/contacts (1).csv'
emails_df = pd.read_csv(file_path)

# Display the first few rows of the dataframe to understand its structure
print(emails_df.head())

# Remove specific email addresses
specific_emails_to_remove = [
    'tkcholdings+email+1fc2g-f3a618bec3@talent.icims.com',
    'jb8mzfisp@jobvite.comdc7+job+1563143844f5b46a90ffabe94cd399019ff9b6d5+514620@app.bamboohr.com',
    'orientaltrading+email+zgh-a91f5a1764@talent.icims.com',
    'c20240419162637KXHFF0SDJZ9Y1LUS@mail.applytojob.com',
    'v3.idibu+2274223a22343931353337222c2263223a2237373622@gmail.com',
    'candidate-7e9f30c6-8b05-45bc-a4f6-17dce829b157@message.teamtailor.com',
    'accommodations-ext@fb.com',
    'beringstraits+email+por-71151397b9@talent.icims.com',
    'julieviaindeed44ky2_22r@indeedemail.com',
    'talentacquisition_support@iem.com'
]

emails_df = emails_df[~emails_df['email'].isin(specific_emails_to_remove)]

# Delete empty rows
emails_df.dropna(subset=['email'], inplace=True)

# Exclude emails from certain domains
domains_to_exclude = ['silverspace', 'zenithinfotech', 'softhq']

def exclude_domains(df, domains):
    pattern = '|'.join([f'@{domain}' for domain in domains])
    return df[~df['email'].str.contains(pattern, case=False, na=False)]

emails_df = exclude_domains(emails_df, domains_to_exclude)

# Example filter functions
def filter_recruiter_emails(df):
    return df[df['email'].str.contains('recruiter', case=False, na=False)]

def filter_bot_emails(df):
    return df[df['email'].str.contains('bot', case=False, na=False)]

def filter_promotional_emails(df):
    promo_keywords = ['promo', 'sale', 'offer', 'discount']
    return df[df['email'].str.contains('|'.join(promo_keywords), case=False, na=False)]

# Filter the emails
recruiter_emails = filter_recruiter_emails(emails_df)
bot_emails = filter_bot_emails(emails_df)
promotional_emails = filter_promotional_emails(emails_df)

# Example operations
def save_filtered_emails(df, filename):
    df.to_csv(filename, index=False)
    print(f"Saved filtered emails to {filename}")

# Save filtered results
save_filtered_emails(recruiter_emails, 'recruiter_emails.csv')
save_filtered_emails(bot_emails, 'bot_emails.csv')
save_filtered_emails(promotional_emails, 'promotional_emails.csv')

# Example of additional operations: counting unique email addresses
unique_emails_count = emails_df['email'].nunique()
print(f"Number of unique emails: {unique_emails_count}")

# Summary statistics
summary = {
    'Total Emails': len(emails_df),
    'Recruiter Emails': len(recruiter_emails),
    'Bot Emails': len(bot_emails),
    'Promotional Emails': len(promotional_emails)
}
print(summary)
