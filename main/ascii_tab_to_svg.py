# John Ecker
# 04/04/2019
# using svgwrite to convert ascii_tabs to svg graphics

import sys
import os
import svgwrite
import requests
import re
from bs4 import BeautifulSoup as bs
# will need to add an import for CSS styling to use w svgWriter

# width and height should be able to be set by user,
# or scale to nearest measure in tab,
# or window size ... eventually

class TabScraper:
    def get_tab(self, url):
        """
        Function to get our tab from the url specified. Uses one pattern now, must be tested
        across more tabs and patterns to ensure that we grab the right tab for our link
        :param url:
        :return:
        """
        # making our soup with page content
        page = bs(requests.get(url).content, features='lxml')

        # this pattern should work for at least some UG pages:
        pattern = 'content":"[^"]*'
        m = re.search(pattern, page.prettify())
        tab = m.group(0)
        return tab



    def process_tab(self, tab):
        """
        Function to process our tab. Not sure how we'll be doing this, so leaving
        empty for now

        One simple start can be to just join the entire tab on /n characters, so we have a
        continuous unbroken represenation of our tab in ASCII. This can then be turned into a
        simple JSON object, or just passed as a string to be handled on the front-end (somehow).

        :return:
        """
        # most of the tabs on UG are split with //n
        lines = tab.split('\\n')
        cleaned_lines = []

        # removing lines without tabs - this will break if there is a note on each
        # line
        for line in lines:
            if '-' in line:
                cleaned_lines.append(line)
        # sorting out our tab into separate lists for each line /string
        strings = []
        for i in range(6):
            strings.append(cleaned_lines[i::6])
        return strings



"""
BASIC ALGORITHM:
0. instantiate base svgwrite.drawing.Drawing() for our tab page
1. break our ascii tab into rows of length "WIDTH"
2. make list of svgwrite.container.SVG() of length num_ascii_rows,
   for each container draw 6 lines of length width, make a factory for this
4. for each ascii_row, parse and fill numbers as text within corresponding
   svgwrite_container
5. write out our svg drawing
"""

# should we make this subclass of svgwrite drawing?
class SVGTab(height, width, style):
    # some other considerations - name, artist, date?
    def __init__(height, width, font_size, css, ascii_tab):
       self.width = width
       self.height = height
       self.size = (height, width)
       self.font_size = font_size
       self.css = css
       self.ascii_tab = ascii_tab
       self.svg_tab = svgwrite.drawing('tab.svg', self.size)
       # note on svgwrtie.drawing size: USER-UNIT is
       # absolute_dimension/relative_dimension
       self.svg_tab.viewbox = self.dimensions


    def break_ascii(ascii_tab, break_lenth):
        """ filling out skeleton method for now """
        # we may not even need to do this
        rows = []
        for string in ascii_tab:
            rows.append(string[::break_length])
        return rows

    def init_row(size, lines = 6):
        """ factory to create tab rows as SVG elements of size=(width, height
            insert position will be set once rows are added to main drawing
        """
        row = self.svg_tab.add(svg_tab.g(id='row',
        # draw lines across our row
        # will start with just basic lines to be naive, eventually will change
        # to rectangles or something more efficient
        for line in lines:
            row.add(self.svg_tab
        return row

    def fill_row(svg_row, ascii_row):
        return filled_row

    def fill_row_text(tab_line):

    def draw_rows(drawing, rows):
        for row in rows:
            drawing.add(row)
        return drawing



def main():
    page = svgwrite.Drawing('tab.svg', size=PAGE_SIZE)
    page.viewbox(0, 0, 80, 80)
    # the page has a size of 20cm x 20cm
    # if we make our viewbox with size of 80x80,
    # size of 1 is 20cm/80 = 0.25cm, USER-UNIT is .25cm

    # using the defs class and setting styling
    # dwg.defs.add(dwg.style(CSS_STYLES))

    # must make a decision on how to draw our
