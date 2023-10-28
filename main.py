import sys

# store {key} {data}                      Store the key value pair in the DB
# get {key}                               Retrieve the value for key. Returns None if it doesnt exist

# Configuration:                                  
# set_threshold {number of bytes}         Set the threshold for the size of the memtable in bytes
# set_sparsity {value}                    Set the sparsity factor for the DBs index
# set_bf_num_items {items}                Set the number of expected items to be stored in the Bloom Filter. Warning: this overrides it.
# set_bf_false_pos_prob {probability}     Set the desired false positive probability for the Bloom Filter. Warning: this overrides it.

# help                                    Print the usage message
# exit                                    Quit the program. Your instance will be saved to disk.

def main():
  print("Toy NoSQL Database")
  while True:
    print('\nEnter commands...\n (Guide)\n [SET VALUE] set `key` `value`\n [GET VALUE] get `key`\n [TERMINATE] exit')
    cmd = input('$ ').lower().split(' ')
    if cmd[0] == 'exit':
      break
    elif len(cmd) == 3 and cmd[0] == 'set':
      print(f'set data key {cmd[1]} value {cmd[2]}')
    elif len(cmd) == 2 and cmd[0] == 'get':
      print(f'get data key {cmd[1]}')
    else:
      print('Invalid command.')

if __name__ == '__main__':
  main()