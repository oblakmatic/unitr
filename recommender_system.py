import numpy as np
import csv
from scipy.sparse import bsr_matrix
from sklearn.model_selection import train_test_split

def write_to_file(filename, text):
    f = open(filename, "w+")
    for line in text:
        line = str(line) + "\n"
        f.write(line)

class Matrix_factorization(object):
    def __init__(self, alpha=0.01, eta=0.01, K=50, users=100, hobbies=90):
        self.alpha = alpha
        self.eta = eta
        self.K = K
        self.users = users
        self.hobbies = hobbies
        self.init_matrices()

    def init_matrices(self):
        self.P = np.random.rand(self.users, self.K) * 0.02 - 0.01
        self.P[:, 0] = np.ones(self.users)  # incorporate bias features
        self.Q = np.random.rand(self.hobbies, self.K) * 0.02 - 0.01
        self.Q[:, 1] = np.ones(self.hobbies)  # incorporate bias features

    def __call__(self, training_data, iter=100, testing=5):
        n = len(training_data)
        rmse_avg = 0
        st = 0

        for t in range(testing):
            num_of_straight_worse_rmse = -1
            rmse = 10000
            self.init_matrices()
            X_train, X_test_last = train_test_split(training_data, test_size=0.3, random_state=42)
            X_train, X_test = train_test_split(X_train, test_size=0.1, random_state=55)

            for i in range(iter):
                for line in X_train:
                    u = int(line[0]) - 1
                    i = int(line[1]) - 1
                    eui = (line[2] - self.P[u].dot(self.Q[i]))
                    pu = self.P[u]
                    self.P[u] = self.P[u] + self.alpha * (eui * self.Q[i] - self.eta * self.P[u])
                    self.P[u][0] = 1  # incorporate bias features
                    self.Q[i] = self.Q[i] + self.alpha * (eui * pu - self.eta * self.Q[i])
                    self.Q[i][1] = 1  # incorporate bias features

                rmse_prev = rmse
                rmse = np.sqrt(np.average(
                    [(line[2] - self.P[int(line[0]) - 1].dot(self.Q[int(line[1]) - 1])) ** 2 for line in X_test]))

                print("tmp rmse: ", rmse)
                st += 1
                if rmse_prev < rmse:
                    break
                    # num_of_straight_worse_rmse += 1
                else:
                    num_of_straight_worse_rmse = 0
                if num_of_straight_worse_rmse > 1:
                    break
            rmse_test = np.sqrt(np.average(
                    [(line[2] - self.P[int(line[0]) - 1].dot(self.Q[int(line[1]) - 1])) ** 2 for line in X_test_last]))
            rmse_avg += rmse_test
        #print("average iterations: ", (st / testing))
        # print(self.P)
        return rmse_avg / testing

    def add_new_user(self, user_data):
        new_P_vector = np.random.rand(self.K) * 0.02 - 0.01
        new_P_vector[0] = 1

        for i in range(13):
            for line in user_data:
                i = int(line[1]) - 1
                eui = (line[2] - new_P_vector.dot(self.Q[i]))
                new_P_vector = new_P_vector + self.alpha * (eui * self.Q[i] - self.eta * new_P_vector)
                new_P_vector[0] = 1  # incorporate bias features
        self.P = np.append(self.P, [new_P_vector], axis=0)
        return new_P_vector

    def recommend_best(self, p_vector):
        ratings = self.Q.dot(p_vector)
        index_array = ratings.argsort()[::-1]
        return index_array, ratings[index_array]

    def get_predicted_hobbies_ratings(self, p_vector):
        return self.Q.dot(p_vector)

    def predict(self, testing_data):
        p = np.array([self.P[int(line[0]) - 1].dot(self.Q[int(line[1]) - 1]) for line in testing_data])
        p[p < 0] = 0
        return p


class Recommender():
    def __init__(self):
        with open('recommender_data/hobbies.dat', 'r', encoding="utf8") as f:
            reader = csv.reader(f, delimiter='\t')
            next(reader)
            hobbies = {}
            for row in reader:
                hobbies[int(row[0])] = row[1]
            print("len(hobbies): ", len(hobbies))

        with open('recommender_data/user_hobbies_training.dat', 'r') as f:
            reader = csv.reader(f, delimiter='\t')
            headers = next(reader)
            train_data = np.array([(int(row[0]), int(row[1]), float(row[2])) for row in reader])
            num = train_data.max(0)
            #print("max: ", num)
            #print("min: ", train_data.min(0))

        self.recommender = Matrix_factorization(users=int(num[0]), hobbies=int(num[1]) + 1)
        error = self.recommender(train_data, testing=1)
        #print("rmse average: ", error)

    def get_all_hobbies(self, new_user_data):
        user_vector = self.recommender.add_new_user(new_user_data)
        #print(user_vector)
        new_vector = self.recommender.get_predicted_hobbies_ratings(user_vector)
        #print(new_vector)
        #print("length:", len(new_vector))
        return new_vector

# THIS IS DEMO FOR GETTING NEW USER'S HOBBIES
if __name__ == "__main__":
    recommender = Recommender()

    with open('recommender_data/new_user_hobbies.dat', 'r') as f:
        reader = csv.reader(f, delimiter='\t')
        next(reader)
        # vectors: [userID, hobbyID, weight]
        new_user_data = np.array([(int(row[0]), int(row[1]), float(row[2])) for row in reader])
        num = new_user_data.max(0)
        print("max: ", num)
        print("min: ", new_user_data.min(0))

    all_hobbies = recommender.get_all_hobbies(new_user_data)
    print("ALL:", all_hobbies)



