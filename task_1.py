class Node:
  def __init__(self, data=None):
    self.data = data
    self.next = None

class LinkedList:
  def __init__(self):
    self.head = None

  def insert_at_beginning(self, data):
    new_node = Node(data)
    new_node.next = self.head
    self.head = new_node
 
  def reverse_list(self):
    prev = None
    cur = self.head

    while cur:
      next_node = cur.next 
      cur.next = prev 
      prev = cur 
      cur = next_node 

    self.head = prev

  def insertion_sort(self):
    if self.head is None or self.head.next is None:
      return
    cur = self.head
    sorted_list = None

    while cur:
      next_node = cur.next
      if sorted_list is None or cur.data < sorted_list.data:
        cur.next = sorted_list
        sorted_list = cur
      else:
        search = sorted_list
        while search.next and search.next.data < cur.data:
          search = search.next
        cur.next = search.next
        search.next = cur
      cur = next_node

    self.head = sorted_list

  def sorted_lists(self, list_1, list_2):
    def merge(node1, node2):
      if node1 is None:
        return node2
      if node2 is None:
        return node1
      
      if node1.data <=node2.data:
        result = node1
        result.next = merge(node1.next, node2)
      else:
        result = node2
        result.next = merge(node1, node2.next)
      return result
    
    return merge(list_1.head, list_2.head)
      
  def print_list(self):
    current = self.head
    while current:
      print(current.data)
      current = current.next

if __name__=="__main__":
    llist = LinkedList()
    llist.insert_at_beginning(5)
    llist.insert_at_beginning(40)
    llist_2= LinkedList()
    llist_2.insert_at_beginning(33)

    llist.print_list()
    llist.reverse_list()
    print("ater reverce:")
    llist.print_list()

    llist.insertion_sort()
    llist_2.insertion_sort()
    
    merget_list = llist.sorted_lists(llist, llist_2)
    while merget_list:
      print(merget_list.data)
      merget_list = merget_list.next