
def statistic(data):
    import pandas as pd

    if type(data)== pd.DataFrame:
        data = data[data.columns[0]]

    description = data.describe()
    values = description.values
    index = description.index

    statistic_summary = pd.DataFrame({ 'Variable': [data.name]})

    zero_count = (data == 0).sum()
    neg_count = (data < 0).sum()

    for key, value in zip(index, values):
        statistic_summary[key.capitalize()] = round(value,2)

    # add manually the Coefficientv of variations (CV)
    statistic_summary['CV'] = round(float(description.loc['std']) / float(description.loc['mean']), 2)

    # add manually the Range and the Interquartile Range (IQR)
    statistic_summary['Range'] = round(float(description.loc['max']) - float(description.loc['min']), 2)
    statistic_summary['IQ Range'] = round(float(description.loc['75%']) - float(description.loc['25%']), 2)

    # add manually the 'Zeros (%)'
    statistic_summary['Zeros (%)'] = f'{round(zero_count / len(data) * 100, 1)} %'

    # add manually the number of negative value
    statistic_summary['Negative (Freq)'] = neg_count

    return statistic_summary 

#------------------------------------------------------------------------------------------------------------------------------

def multi_statistic(data):
    import pandas as pd
    statistic_summary = pd.DataFrame({ 'Variable': []})
    # iterate through dataset columns and add a statistics row for each variable/column
    for var in data.columns:

        description = data[var].describe().apply(lambda x: '%.2f' % x)
        values = description.values
        index = description.index

        zero_count = (data[var] == 0).sum()
        neg_count = (data[var] < 0).sum()

        new_data = {
            'Variable': str(data[var].name)
        }
        for key, value in zip(index, values):
            new_data[key.capitalize()] = value

        new_data['CV'] = round(float(description['std']) / float(description['mean']), 2)
        new_data['Range'] = round(float(description['max']) - float(description['min']), 2)
        new_data['IQ Range'] = round(float(description['75%']) - float(description['25%']), 2)
        new_data['Zeros (%)'] = f'{round(zero_count / len(data) * 100, 1)} %'
        new_data['Negative (Freq)'] = neg_count

        statistic_summary = statistic_summary.append(new_data, ignore_index=True)

    return statistic_summary 

#------------------------------------------------------------------------------------------------------------------------------


def gender_statistic(data):
    from collections import Counter
    import pandas as pd

    n = len(data)  
    gender_count = Counter(data)
    gender_summary = pd.DataFrame({ data.name.capitalize(): [], 'Frequency':[] , 'Percentage':[]})

    cumulative_freq , cumulative_perc = 0, 0

    for key, count in gender_count.most_common(3):

        # if the gender_name == '' replace the name with 'Missing Value'
        if key == '':
            new_data = {
                data.name.capitalize(): 'Missing value',
                'Frequency': count,
                'Percentage': f'{round(count / n *100, 2)} %',
            }
            gender_summary = gender_summary.append(new_data, ignore_index=True)
    
        # add the couple of key-frequency in the dataframe and calculate manually the Percentage
        else:
            new_data = {
                data.name.capitalize(): str(key).capitalize(),
                'Frequency': count,
                'Percentage': f'{round(count / n *100, 2)} %',
            }
            gender_summary = gender_summary.append(new_data, ignore_index=True)

        # save locally the cumulative Percentage and the cumulative frequency
        cumulative_perc += round(count/n,3)
        cumulative_freq += count

    # aggregate all the other gender into one bin called 'other'
    new_data = {
        data.name.capitalize(): 'Other',
        'Frequency': n - cumulative_freq,
        'Percentage': f'< {round((1 - cumulative_perc) *100 , 3)} %',
    }
    gender_summary = gender_summary.append(new_data, ignore_index=True)
    return gender_summary

#------------------------------------------------------------------------------------------------------------------------------

def qualitative_statistic(data , n_levels):
    from collections import Counter
    import pandas as pd

    n= len(data)
    var_count = Counter(data[data.columns[0]])
    statistic_summary = pd.DataFrame({ data.columns[0].capitalize(): [], 'Frequency':[] , 'Percentage':[]})

    cumulative_freq , cumulative_perc = 0, 0

    for key, count in var_count.most_common((n_levels-1)):

    # if the level_name == '' replace the name with 'Missing Value'
        if key == '':
            new_data = {
                data.columns[0].capitalize(): 'Missing value',
                'Frequency': count,
                'Percentage': f'{round(count / n *100, 2)} %',
            }
            statistic_summary = statistic_summary.append(new_data, ignore_index=True)
    
        # add the couple of key-frequency in the dataframe and calculate manually the Percentage
        else:
            new_data = {
                data.columns[0].capitalize(): str(key).capitalize(),
                'Frequency': count,
                'Percentage': f'{round(count / n *100, 2)} %',
            }
            statistic_summary = statistic_summary.append(new_data, ignore_index=True)

        # save locally the cumulative Percentage and the cumulative frequency
        cumulative_perc += round(count/n,3)
        cumulative_freq += count

    # aggregate all the remaining publisher into one bin called 'other'
    new_data = {
        data.columns[0].capitalize(): 'Other',
        'Frequency': n - cumulative_freq,
        'Percentage': f' {round((1 - cumulative_perc) *100 , 3)} %',
    }
    statistic_summary = statistic_summary.append(new_data, ignore_index=True)
    

    return statistic_summary

#------------------------------------------------------------------------------------------------------------------------------

def pages_statistic(data):
    import pandas as pd
    data[data.columns[0]] = pd.to_numeric(data[data.columns[0]], errors='coerce')

    righe_negative = data[data[data.columns[0]] < 0]
    neg_count = len(righe_negative)

    if type(data)== pd.DataFrame:
        data = data[data.columns[0]]

    description = data.describe()
    values = description.values
    index = description.index

    statistic_summary = pd.DataFrame({ 'Variable': [data.name]})

    zero_count = (data == 0).sum()
    
    for key, value in zip(index, values):
        statistic_summary[key.capitalize()] = round(value,2)

    # add manually the Coefficientv of variations (CV)
    statistic_summary['CV'] = round(float(description.loc['std']) / float(description.loc['mean']), 2)

    # add manually the Range and the Interquartile Range (IQR)
    statistic_summary['Range'] = round(float(description.loc['max']) - float(description.loc['min']), 2)
    statistic_summary['IQ Range'] = round(float(description.loc['75%']) - float(description.loc['25%']), 2)

    # add manually the 'Zeros (%)'
    statistic_summary['Zeros (%)'] = f'{round(zero_count / len(data) * 100, 1)} %'

    # add manually the number of negative value
    statistic_summary['Negative (Freq)'] = neg_count

    return statistic_summary 


#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def allTheYears(df):
    import pandas as pd
    from collections import defaultdict
    import re
    import calendar

    years_set = set() # set to store the years

    def sort_years(item): # this function is used to sort the years in increasing order
        return (len(item), item)

    valid_dates = df[df['publication_date'].str.match(r'([1-9]{1}\d{0,3})(-\d{2}){1,2}')] # use a regual expression to filter valid dates 
    years = valid_dates['publication_date'].str.split("-").str[0] # extract the year splitting on "-"
    years_set.update(years) # add the years to the set 
        
    years_list = [year for year in years_set if int(year) < 2024]   # create a new list with years <= current year
    years_list = sorted(years_list, key=sort_years)  

    return years_list

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def get_books_by_author(author_ids, df):

    """
        Args: 
        
            author_ids: a list of the unique IDs of the authors

            df_authors: the authors data frame 

        returns: a dictionary of key equals to the author's ID and value equals to the books IDs of the books written by that author.

    """
    author_book_dict = {}

    #grouping and concatenating book IDs by author ID
    author_book_dict = (
        df[df['id'].isin(author_ids)]
        .groupby('id')['book_ids']
        .apply(lambda x: x.tolist())
        .apply(lambda x: [item for sublist in x for item in sublist])
        .to_dict()
    )
    return author_book_dict

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def get_top_rated_authors(df):

    # sorting the dataframe based on the average rating
    df = df.sort_values(by = 'average_rating', ascending=False)

    # find the top 20 rated authors
    top_rated_authors = df.head(20)

    # making a list of the IDs of top 20 rated authors
    top_rated_ids = top_rated_authors['id'].tolist()

    return top_rated_ids

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def year_date(date_str):
    import pandas as pd
    try:
        date = pd.to_datetime(date_str, errors='coerce')
        return date.strftime('%Y') if not pd.isna(date) else None
    except:
        return None