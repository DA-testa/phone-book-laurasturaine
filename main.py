# python3

class Contact:
    def __init__(self, type_, number, name):
        self.type = type_
        #self.type = query[0]
        self.number = number
        #if self.type == 'add':
        self.name = name

#def read_queries():
  #  n = int(input())
  #  return [Query(input().split()) for i in range(n)]

def write_responses(result):
    for r in result:
        print(r)
  #  print('\n'.join(result))

def process_queries(queries):
    result = []
    # Keep list of all existing (i.e. not deleted yet) contacts.
    contacts = {}
    for cur_query in queries:
        if cur_query.type == 'add':
            contacts[cur_query.number]=cur_query.name
        elif cur_query.type == 'del':
            if cur_query.number in contacts:
                del contacts[cur_query.number]
        else:
            name = contacts.get(cur_query.number, 'not found')
            result.append(name)
    return result
            # if we already have contact with such number,
            # we should rewrite contact's name
            #for contact in contacts:
               # if contact.number == cur_query.number:
                   # contact.name = cur_query.name
                   # break
            #else: # otherwise, just add it
               # contacts.append(cur_query)
       # elif cur_query.type == 'del':
            #for j in range(len(contacts)):
               # if contacts[j].number == cur_query.number:
                   # contacts.pop(j)
                   # break
        #else:
           # response = 'not found'
            #for contact in contacts:
                #if contact.number == cur_query.number:
                   # response = contact.name
                  #  break
            #result.append(response)
    #return result


if __name__ == '__main__':
    inp=int(input())
    queries =[]
    for i in range(inp):
        query = input().split()
        if query[0] =='add':
            queries.append(Contact(query[0], int(query[1]), query[2]))
        else:
            queries.append(Contact(query[0], int(query[1]), None))
    write_responses(process_queries(queries))

