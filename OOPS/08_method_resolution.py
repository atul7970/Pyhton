# class a:
#     def processing(self,text):
#         return [item.strip() for item in text.split(",")]

# s = "apple, banana, cherry"

# b = a()

# print(b.processing(s))


class a:
    @staticmethod
    def processing(text):
        return [item.strip() for item in text.split(",")]

s = "apple, banana, cherry"

print(a.processing(s))
