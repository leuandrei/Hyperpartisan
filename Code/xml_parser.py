import re

path_to_articles = 'articles-training-20180831.xml'
xml_file = open(path_to_articles, 'r')
xml_out = open(r'xml_out.xml', 'w')
parsed_xml = open(r'parsed_xml.txt', 'w')

bytes_to_read = 90000
data = xml_file.read(bytes_to_read)
xml_out.write(data)

article_regex = re.compile('(<article.*?>.*?</article>)', re.DOTALL)
get_title_from_article_regex = re.compile('title=\"(.*?)\"')
p_tag_regex = re.compile('<p>(.*?)</p>')
a_tag_regex = re.compile('(<a.*?>.*?</a>)')
a_tag_content_regex = re.compile('<a.*?>(.*?)</a>')

articles = article_regex.findall(data)

for article in articles:
    parsed_xml.write(get_title_from_article_regex.findall(article)[0])
    parsed_xml.write('\n\n')
    ps = p_tag_regex.findall(articles[0])
    for i in range(0, len(ps)):
        a_tags = a_tag_regex.findall(ps[i])
        a_tags_content = a_tag_content_regex.findall(ps[i])
        for j in range(0, len(a_tags)):
            ps[i] = ps[i].replace(a_tags[j], a_tags_content[j])
        parsed_xml.write(ps[i])
        parsed_xml.write('\n')
    parsed_xml.write('\n\n')

parsed_xml.close()
xml_out.close()
