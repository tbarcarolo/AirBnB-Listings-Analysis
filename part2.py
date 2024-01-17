import pandas as pd
import matplotlib.pyplot as plt

p2 = pd.read_csv('airbnb_listings.csv')

def display_menu():
    print("\n------ Airbnb Happiness Explorer ------\n")
    print("1. 📚 Unveil the secrets of the Airbnb dataset")
    print("2. 🏡 Give me a sneak peek of the Airbnb wonderland")
    print("3. 📊 Let's dive into the fascinating statistics")
    print("4. 🌠 Illuminate the histogram of review scores rating")
    print("5. 🏰 Unveil the magical distribution of property types")
    print("6. 🥇 Present the VIP hosts with the most listings")
    print("7. 🌟 Show me the top 10 rated, magical Airbnbs for at least 8 enchanted nights and instantly bookable")
    print("8. 🧹 Share the cleanliness rating spells for listings 12-15")
    print("9. 🎨 Display a vibrant bar chart representing the distribution of room types")
    print("10. 🌈 Provide the average review scores for the listings 20-25")
    print("11. 🚪 Exit the enchanted world")

def plot_histogram(data, title, xlabel, ylabel):
    data.plot(kind='hist', bins=20, edgecolor='black')
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()

def analyze_property_types():
    property_counts = p2['property_type'].value_counts()
    property_counts.plot(kind='bar', color='red')
    plt.title('Distribution of Property Types')
    plt.xlabel('Property Type')
    plt.ylabel('Count')
    plt.xticks(rotation=45, ha='right')
    plt.show()

def top_hosts_by_listings():
    top_hosts = p2.groupby('host_id')['id'].count().nlargest(5)
    top_hosts.plot(kind='bar', color='green')
    plt.title('Top 5 Hosts with the Most Listings')
    plt.xlabel('Host ID')
    plt.ylabel('Number of Listings')
    plt.show()

def top_rated_airbnbs():
    top_rated = p2[(p2['minimum_nights'] >= 8) & (p2['instant_bookable'] == 't')].nlargest(10, 'review_scores_rating')
    print("\nTop 10 Rated, Enchanting Airbnb's for at least 8 nights and instantly bookable:\n")
    print(top_rated[['name', 'review_scores_rating']])

def cleanliness_rating_listings_12_15():
    cleanliness_ratings = p2.loc[11:14, ['name', 'review_scores_cleanliness']]
    print("\nCleanliness Rating Spells for Listings 12-15:\n")
    print(cleanliness_ratings)

def room_type_distribution_chart():
    room_type_counts = p2['room_type'].value_counts()
    room_type_counts.plot(kind='bar', colormap='Spectral')
    plt.title('Distribution of Room Types')
    plt.xlabel('Room Type')
    plt.ylabel('Count')
    plt.xticks(rotation=0)
    plt.show()

def average_review_scores_listings_20_25():
    average_review_scores = p2.loc[19:24, ['name', 'review_scores_rating']]
    print("\nAverage Review Scores for the Fairy-Tale Listings 20-25:\n")
    print(average_review_scores)

def dataset_explanation():
    print("\n📚 Behold! Let me unveil the secrets of the magical dataset:")
    print("\nThis enchanting dataset consists of 7566 AirBnB listings with a variety of qualitative and quantitative variables.")
    print("It contains information about cozy cottages, magical rooms, and much more! Explore the wonders:\n")
    print(p2.info())

def main():
    while True:
        display_menu()
        choice = input("\nEnter your choice (1-11): ")

        if choice == '1':
            dataset_explanation()
        elif choice == '2':
            print("\n👀 Welcome to the Airbnb Wonderland! Here's a sneak peek:\n")
            print(p2.head())
        elif choice == '3':
            print("\n📊 Let's dive into the fascinating statistics:\n")
            selected_columns = ['accommodates', 'bedrooms', 'beds', 'price', 'review_scores_rating']
            print(p2[selected_columns].describe())
        elif choice == '4':
            plot_histogram(p2['review_scores_rating'], 'Histogram of Review Scores Rating', 'Rating', 'Frequency')
        elif choice == '5':
            analyze_property_types()
        elif choice == '6':
            top_hosts_by_listings()
        elif choice == '7':
            top_rated_airbnbs()
        elif choice == '8':
            cleanliness_rating_listings_12_15()
        elif choice == '9':
            room_type_distribution_chart()
        elif choice == '10':
            average_review_scores_listings_20_25()
        elif choice == '11':
            print("\n🚪 Leaving the enchanted world. Farewell!\n")
            break
        else:
            print("\n😅 Oops! Invalid choice. Please enter a valid option.\n")

if __name__ == "__main__":
    main()
