from requests import get


def load_course_data():
    cbl_site = "https://cobalt.qas.im/api/1.0/courses"
    net_key = "mYsO2m1KfJYFBEd3BYVvho4bmI9PKR2x"
    start_term = "2017 Fall"
    filters = "code:\"CSC\" AND campus:\"UTSG\" AND term:>=\"{0}\"".format(start_term)
    skip_amt = 100
    params = "&limit={0}".format(skip_amt)

    request_base = "{0}/filter?key={1}&q={2}{3}".format(cbl_site, net_key, filters, params)

    passed_count = 0
    combined = []
    new_data = None
    while new_data != []:
        request = request_base + "&skip={0}".format(passed_count)
        new_data = get(request).json()
        combined.extend(new_data)
        passed_count += 100

    return combined


if __name__ == '__main__':
    load_course_data()