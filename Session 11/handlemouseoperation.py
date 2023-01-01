"""
Mouse Operation

=> We use the class called ActionChains(driver)

There are 4 operation
1. Mouse hover - placing the mouse on an element then the rest of the option are displayed.
                 use move_to_element(element).perform()
2. Right click -  used to perform right click
                  use context_click(element).perform()
3. Double click - used to perform double click
                  use double_click(element).perform()
4. Drag and drop - used to perform drag and drop operations
                  use drag_and_drop(source_box,target_box).perform()
5. Drag and drop by offset - used to perform drag and drop operation by giving the values, eg: for sliders.
                             used drag_and_drop_by_offset(max_sli, xoffset, yoffset).perform()

=> Scrolling page -  mouse operation done without using ActionChains
"""


