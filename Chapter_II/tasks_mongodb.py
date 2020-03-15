from pymongo import MongoClient
from errors import MissingValueError
import argparse
import datetime
import hashlib

parser = argparse.ArgumentParser(description="Handle your task database")
parser.add_argument('action_type')
parser.add_argument('--task_hash')
parser.add_argument('--name')
parser.add_argument('--deadline')
parser.add_argument('--description')
parser.add_argument('--all', action='store_true')
parser.add_argument('--today', action='store_true')
args = parser.parse_args()

client = MongoClient(
    "mongodb+srv://root:root@tasks-i863j.mongodb.net/test?retryWrites = true & w = majority")

db = client.get_database('tasks_db')
records = db['task_records']


def add(task_name, deadline, description):
    hashed_name = hashlib.sha256(str(task_name).encode('utf-8')).hexdigest()
    new_task = {
        "name": task_name,
        "deadline": datetime.datetime.strptime(deadline, "%Y-%m-%d"),
        "descripition": description,
        "task_hash": hashed_name
    }
    records.insert_one(new_task)


def update(hashed_name, **update_variables):
    search_query = {"task_hash": hashed_name}
    new_values = {}
    for key, value in update_variables.items():
        new_values[key] = value
    hashed_name = hashlib.sha256(str(new_values['name']).encode('utf-8')).hexdigest()
    new_values['task_hash'] = hashed_name
    update_query = {"$set": new_values}
    updated_records = records.update_one(search_query, update_query)
    if updated_records.matched_count == 0:
        print("No tasks with this hash")
    elif updated_records.modified_count > 0:
        print("Successfully modified " + updated_records.modified_count + " records")


def remove(hashed_name):
    query = {"task_hash": hashed_name}
    records.delete_one(query)


def list(listing_argument):
    if listing_argument == "all":
        db_cursor = records.find()
        for record in db_cursor:
            print('*'*74)
            for key, value in record.items():
                print(key, value)
    elif listing_argument == "today":
        db_cursor = records.find()
        for key, value in db_cursor.next().items():
            if x.deadline == datetime.date.today():
                print(key, value)


if __name__ == "__main__":
    action = args.action_type
    if action:
        if action == 'add':
            if args.name:
                add(args.name, args.deadline, args.description)
            else:
                raise MissingValueError("Please add name of your tasks")

        if action == 'remove':
            if args.task_hash:
                remove(args.task_hash)
            else:
                raise SyntaxError("Please add task hash for your query.")

        if action == 'update':
            if args.task_hash:
                update(args.task_hash,
                       name=args.name,
                       description=args.description,
                       deadline=args.deadline)
            else:
                raise SyntaxError("Please add task hash for your query.")

        if action == 'list':
            if args.all:
                list('all')
            elif args.today:
                list('today')
            else:
                raise MissingValueError("Please add a switch to list query.")
    else:
        raise SyntaxError('Please include action type of query')
