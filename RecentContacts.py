import array

class RecentContacts(object):
    
    # haw many contacts can be stored in the list
    __serializationSeparator = "<*>"

    # haw many contacts can be stored in the list
    __historyDepth = 15

    # a list of recent contacts
    __recentContactsList = []


    # constructor
    def __init__(self, histDepth):

        self.__historyDepth = histDepth

        self.__recentContactsList = []

        return;

    #def __init__(self, histDepth, history):

    #    self.__historyDepth = histDepth

    #    self.__recentContactsList = history

    #    self.__trimHistory(self)

    #    return;
    
    #def __init__(self, histDepth, fileName, contactFromoStringMethod):

    #    self.__historyDepth = histDepth

    #    self.ReadHistory(self, contactFromoStringMethod, fileName)

    #    self.__trimHistory(self)

    #    return;


    # removing redundant tail
    def __trimHistory(self):

        self.__recentContactsList = self.__recentContactsList[0:min(len(self.__recentContactsList)-1, self.__historyDepth-1)]

        return

    # add a new contact to the list (to the head) and trim the history
    def AddContat(self, contact:object):

        self.__recentContactsList.insert(0, contact)

        self.__trimHistory()

        return
    
    def ClearHistory(self):

        ok = input('  Are you really wabt to clear the history?') == 'yes'

        if ok:

            self.__recentContactsList = []

        else:

            print('   ok... aborted')

        return


    def PrintRecentContacts(self):

        if len(self.__recentContactsList) < 1:

        print('You have following recent contacts:')

        for c in self.__recentContactsList:

            print('  ' + c) # shows the contact

        return

    def SaveHistory(self, contactToStringMethod, fileName:str):

        with open(fileName, 'w') as f:

            for c in self.__recentContactsList:

                f.wri(contactToStringMethod(c) + "\n")

        return

    def ReadHistory(self, contactFromoStringMethod, fileName:str):

        self.__recentContactsList = []

        with open(fileName, 'r') as f:

            lines = [line.rstrip() for line in f]

            for line in lines:

                try:
                    
                    contact = contactFromoStringMethod(line)

                    self.__recentContactsList.insert(0, contact)

                    break

                except:

                    print(' ' + type(self).__name__ + ': can not parse the contact object' + '\n' + 
                          '    ' + temp)
                    
                    continue

        return

    pass