# Simple Firestore Import

Easily import data into Firebase Cloud Firestore from json and yaml files.

## Installation

Clone the repo:

    $ git clone https://github.com/RobinCheptileh/simple-firestore-import.git

Move into the directory:

    $ cd simple-firestore-import

## Usage

    $ simple-firestore-import.py [path/to/serviceAccount.json] [path/to/dataFile(.json|.yaml|.yml)] [name of collection]
    
Or without arguments:

    $ simple-firestore-import.py
    Path to serviceAccountKey.json: [path/to/serviceAccount.json]
    Path to data file: [path/to/dataFile(.json|.yaml|.yml)]
    Name of collection: [name of collection]
    
#### Note

The program expects an array of objects (dictionaries) to work.

**CORRECT DATA FILE FORMAT**

```json
[
    {
        "name": "Jane Doe",
        "email": "janedoe@mail.com"
    },
    {
        "name": "John Doe",
        "email": "johndoe@mail.com"
    }
]
```

```yaml

---
- name: Jane Doe
  email: janedoe@mail.com
- name: John Doe
  email: johndoe@mail.com
```

## Contributing

Bug reports and pull requests are welcome on GitHub at https://github.com/robincheptileh/simple-firestore-import. This project is intended to be a safe, welcoming space for collaboration, and contributors are expected to adhere to the [Contributor Covenant](http://contributor-covenant.org) code of conduct.

## License

The program is available as open source under the terms of the [MIT License](http://opensource.org/licenses/MIT).

## Code of Conduct

Everyone interacting in the Simple Firestore Import project’s codebases, issue trackers, chat rooms and mailing lists is expected to follow the [code of conduct](https://github.com/robincheptileh/simple-firestore-import/blob/master/CODE_OF_CONDUCT.MD).