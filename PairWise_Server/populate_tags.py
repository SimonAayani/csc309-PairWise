from PairWise_Server.models.data_tags import LanguageTag, ConceptTag, FrameworkTag, LocationTag
from django.db.transaction import atomic

language_options = [
        'Assembly',
        'Bash',
        'C',
        'C++',
        'C#',
        'Haskell',
        'HTML',
        'Java',
        'JavaScript',
        'MATLAB',
        'Pascal',
        'Perl',
        'PHP',
        'Prolog',
        'Python',
        'R',
        'Racket',
        'Ruby',
        'SQL',
        'Swift',
        'Unity',
        'Verilog',
        'VHDL'
    ]

concept_options = [
        'Algorithm Design',
        'Artificial Intelligence',
        'Backend Development',
        'Compilers',
        'Computer Graphics',
        'Concurrency',
        'Data Structures',
        'Database Systems',
        'Frontend Development',
        'Functional Programming',
        'Hardware',
        'Machine Learning',
        'Object-Oriented Design',
        'Software Process',
        'UI/UX Design',
    ]

framework_options = [
        'Android',
        'Angular',
        'Bootstrap',
        'Django',
        'Flask',
        'JQuery',
        'MongoDB',
        'MySQL',
        '.NET',
        'Node',
        'Oracle',
        'PostgreSQL',
        'Pyramid',
        'React',
        'Rails',
    ]

location_options = [
        'BA3200',
        'Brampton',
        'Downtown',
        'East York',
        'Etobikoke',
        'Markham',
        'Mississauga',
        'North York',
        'Richmond Hill',
        'Scarborough',
        'Vaughan',
        'York',
    ]

def load_tags(data, dest_class):
    if type(data[0]) == str:
        for i in range(len(data)):
            data[i] = dest_class(tag_text=data[i])

    with atomic():
        for datapoint in data:
            datapoint.save()


if __name__ == '__main__':
    load_tags(language_options, LanguageTag)
    load_tags(concept_options, ConceptTag)
    load_tags(framework_options, FrameworkTag)
    load_tags(location_options, LocationTag)
    print('Done')