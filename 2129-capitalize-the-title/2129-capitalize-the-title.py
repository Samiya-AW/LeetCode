class Solution:
    def capitalizeTitle(self, title: str) -> str:
        
        title_list = title.split(' ')

        for w in range(len(title_list)):
            if len(title_list[w]) <= 2:
                title_list[w] = title_list[w].lower()
            else:
                title_list[w] = title_list[w].title()
        
        return ' '. join(title_list)
                