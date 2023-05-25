import random

# Get the number of Facebook friends
num_friends = 1400

# Create a list of demographics
demographics = [
    "Male",
    "Female",
    "Others"
]

# Create a list of age groups
age_groups = [
    "18-24 years",
    "25-34 years",
    "35-44 years",
    "45-54 years",
    "55+ years"
]

# Create a list of ethnicities
ethnicities = [
    "African-American",
    "Caucasian",
    "Hispanic/Latino",
    "Asian",
    "Others"
]

# Create a list of health and fitness interests
health_and_fitness_interests = [
    "Engaged in regular exercise",
    "Interested in nutrition and healthy eating",
    "Actively seeking health and wellness programs",
    "Open to exploring spiritual connections with health"
]

# Create a list of social engagements
social_engagements = [
    "Actively participate in online health-related communities",
    "Engage in group activities",
    "Attend church or religious gatherings"
]

# Create a list of income and education levels
income_and_education_levels = [
    "Varying income levels",
    "Varying educational backgrounds"
]

# Create a dictionary to store the demographics, age groups, ethnicities, health and fitness interests, social engagements, and income and education levels
personas = {
    "demographics": demographics,
    "age_groups": age_groups,
    "ethnicities": ethnicities,
    "health_and_fitness_interests": health_and_fitness_interests,
    "social_engagements": social_engagements,
    "income_and_education_levels": income_and_education_levels
}

# Create a list of synthetic individuals
synthetic_individuals = []

# For each Facebook friend:
for friend in range(num_friends):

    # Generate a random demographic
    demographic = random.choice(demographics)

    # Generate a random age group
    age_group = random.choice(age_groups)

    # Generate a random ethnicity
    ethnicity = random.choice(ethnicities)

    # Generate a random health and fitness interest
    health_and_fitness_interest = random.choice(health_and_fitness_interests)

    # Generate a random social engagement
    social_engagement = random.choice(social_engagements)

    # Generate a random income and education level
    income_and_education_level = random.choice(income_and_education_levels)

    # Create a synthetic individual
    synthetic_individual = {
        "demographic": demographic,
        "age_group": age_group,
        "ethnicity": ethnicity,
        "health_and_fitness_interest": health_and_fitness_interest,
        "social_engagement": social_engagement,
        "income_and_education_level": income_and_education_level
    }

    # Add the synthetic individual to the list
    synthetic_individuals.append(synthetic_individual)

# Return the list of synthetic individuals
return synthetic_individuals
