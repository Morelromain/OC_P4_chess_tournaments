"""Results view"""


class ViewDB:
    """View all player database"""

    def display_all_p(self, list_a):
        """View all player database"""
        for nb in range(len(list_a)):
            print(list_a[nb])

    def display_all_t(self, p_tab):
        """View all player database"""
        alldata_t = p_tab.all()
        for nb in range(len(alldata_t)):
            print(alldata_t[nb])
