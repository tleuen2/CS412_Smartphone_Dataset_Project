import numpy as np
import pprint

debug = True

training_labels = np.genfromtxt('train.csv', delimiter = ",", usecols = -1, dtype = 'unicode', skip_header = 1, autostrip = True)
training_data = np.genfromtxt('train.csv', delimiter = ",", skip_header = 1)[:,:-1]
#print(train)

# Data structure to hold sorted data
class phoneData:

    def __init__(self):
        self.data_dict = {}
        self.mean_vectors = {}        
        
    def add_class(self, label):
        # Each label has its own array of values
        self.data_dict[label] = []
        self.mean_vectors[label] = []

    def add_row(self, label, row):
        # Stack the new row into our data array
        if len(self.data_dict[label]) >= 1:
            self.data_dict[label] = np.vstack((self.data_dict[label], row))
        else:
            self.data_dict[label] = row
        
    def should_class_be_added(self, label):
        if label in self.data_dict:
            return False
        else:
            return True
            
    def calculate_mean_vector(self):
        for label in self.mean_vectors:
            
            
    def show_info(self):
        print('---------Info about data containter---------')
        print('*Number of Classes = ', len(self.data_dict.keys()))
        for j in self.data_dict:
            print('*The shape of label ' , j , ' is ' , self.data_dict[j].shape)
        print('---------Info about data containter---------')
    
def seperate_by_class(labels, data):
    # each label is given in the last column of the data table
    # As such we need to divide the data baised on the values in the last column
    my_data = phoneData()
    # There is an implict ordering of the parsed file...
    for i in range(len(labels)):
        if (my_data.should_class_be_added(labels[i]) == True):
            my_data.add_class(labels[i])
        my_data.add_row(labels[i], data[i])        
    return my_data
        

def get_mean_vector(my_data):
    ret_val = {}
    for key in 

def main():
    train_data = seperate_by_class(training_labels, training_data)
    train_data.show_info()
    

if __name__ == '__main__':
    main()
    