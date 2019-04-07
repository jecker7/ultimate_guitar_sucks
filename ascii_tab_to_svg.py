# John Ecker
# 04/04/2019
# using svgwrite to convert ascii_tabs to svg graphics

import sys
import os
import svgwrite
import requests
import re
import numpy as np
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
        processing ascii tab by removing text and special chars not displayed
        on the tab and joining on newline
        :return: strings, a list containing the six unbroken lines of the tab
        """
        # fixing slide notation
        tab = tab.replace('\/','/')
        # most of the tabs on UG are split with //n
        lines = tab.split('\\r\\n')
        cleaned_lines = []
        # removing lines without tabs - this will break if there is a note on each
        # line
        for line in lines:
            if '-' in line:
                cleaned_lines.append(line)
        # sorting out our tab into separate lists for each line /string
        # eventually we'll want to support numba. for now a 2d numpy array
        # will do to represent our tab, but eventually we will need to switch
        # to passing in the strings as *args of numpy lists
        # for full optimization, strings will need to be represented as
        # numerical char arrays
        strings = []
        for i in range(6):
            strings.append(cleaned_lines[i::6])
        for i, string in enumerate(strings):
            strings[i] = ''.join(string)

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
class SVGTab:
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

    def tab_poly_points(start, height, width, line_spacing):
        """ generates polyline points for building a simple 6-line staff
            todo: do this iteratively for n number of lines
        """
        points = []
        points.append((start[0], start[1]))
        points.append((start[0]+width, start[1]))
        points.append((start[0]+width, start[1]+line_spacing))
        points.append((start[0], start[1]+line_spacing))
        points.append((start[0], start[1]+ line_spacing*2))
        points.append((start[0]+width, start[1]+line_spacing*2))
        points.append((start[0]+width, start[1]+line_spacing*3))
        points.append((start[0], start[1]+ line_spacing*3))
        points.append((start[0], start[1]+ line_spacing*4))
        points.append((start[0]+width, start[1]+line_spacing*4))
        points.append((start[0]+width, start[1]+line_spacing*5))
        points.append((start[0], start[1]+ line_spacing*5))
        points.append((start[0]+width, start[1]+line_spacing*5))
        points.append((start[0], start[1]))
        points.append((start[0]+width, start[1]))
        points.append((start[0]+width, start[1]+line_spacing*5))
        return points

    def fill_staff(svg_drawing, ascii_tab, start_x, start_y, line_spacing, drawing, font_size
                   staff_width, staff_spacing):
        """ fills an svg tab with the notes from an ascii tab """
        cur_x = start_x
        cur_y = start_y
        # note: this function will vary if we're starting on top vs bottom
        # string in our ascii tab
        for staff in staff_rows:
            for line in ascii_tab:
                for char in line:
                    if char.isdigit():
                    svg_drawing.add(svg_drawing.text(char, x=cur_x, y=cur_y))
                    cur_x += 1
                cur_y += line_spacing
                cur_x = start_x
            cur_y += staff_spacing

def main():
    page = svgwrite.Drawing('tab.svg', size=PAGE_SIZE)
    page.viewbox(0, 0, 80, 80)
    # the page has a size of 20cm x 20cm
    # if we make our viewbox with size of 80x80,
    # size of 1 is 20cm/80 = 0.25cm, USER-UNIT is .25cm

    # using the defs class and setting styling
    # dwg.defs.add(dwg.style(CSS_STYLES))

    # must make a decision on how to draw our
