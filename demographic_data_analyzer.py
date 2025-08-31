import pandas as pd

def calculate_demographic_data(print_data=True):
    # Leer el archivo CSV
    df = pd.read_csv("adult.data.csv")

    # Cantidad de personas por raza
    race_count = df['race'].value_counts()

    # Edad promedio de los hombres
    average_age_men = round(df[df['sex'] == 'Male']['age'].mean(), 1)

    # Porcentaje de personas con título universitario (Bachelors)
    percentage_bachelors = round((df['education'] == 'Bachelors').mean() * 100, 1)

    # Educación avanzada
    higher_education = df[df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
    lower_education = df[~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]

    # Porcentaje de personas con educación avanzada que ganan >50K
    higher_education_rich = round((higher_education['salary'] == '>50K').mean() * 100, 1)
    lower_education_rich = round((lower_education['salary'] == '>50K').mean() * 100, 1)

    # Mínimo de horas trabajadas por semana
    min_work_hours = df['hours-per-week'].min()

    # Porcentaje de personas que trabajan el mínimo y ganan >50K
    min_workers = df[df['hours-per-week'] == min_work_hours]
    rich_percentage = round((min_workers['salary'] == '>50K').mean() * 100, 1)

    # País con mayor porcentaje de personas que ganan >50K
    country_salary = df.groupby('native-country')['salary'].value_counts(normalize=True).unstack()
    country_salary = country_salary.fillna(0)
    highest_earning_country_percentage = round(country_salary['>50K'].max() * 100, 1)
    highest_earning_country = country_salary['>50K'].idxmax()

    # Ocupación más común entre los que ganan >50K en India
    top_IN_occupation = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]['occupation'].mode()[0]

    # Salida opcional
    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage': highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
