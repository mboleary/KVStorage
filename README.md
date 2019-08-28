# JSON Key/Value Pair Storage Script

This script allows for easy persistent storiage of Keys and Values into a JSON file.

This program is designed to __NOT FAIL__. This means that if a bad key is supplied, then the program will print nothing and exit.

## Commands

The command schema is designed to be atomic to allow for easy parsing.
It supports the following commands...

### View

`-v <KeyName>`

__Note:__ if this command is the first, then do not require the flag only for the first instance.

View a Value from a given Key. If the key does not exist, then nothing will print out (It fails silently).

### Save

`-w <KeyName> <NewValue>`

Save a new Value with a given Key. If the key doesn't exist, then one will be created.

### Delete

`-d <KeyName>`

Delete a Value and Key Pair. If the key doesn't exist, then nothing will happen.

### Search

`-s <SearchString>`

Search for keys with a given search value.

### Get Keys

`-k [<KeyName>]`

Display all of the keys at the current level

## Usage

`kv.py <JSON File> [<Command Atom>]`

KV Supports performing multiple operations on the JSON File, but only for certain ones. If a Strictly-Single Operation, then the first one found will be used and then the program will exit.

`kv.py <JSON File> ...`

Strictly-Single Operations:

`[-s <SearchString>]` - Search for a string in the keys

`[-k]` - Display all of the keys

`-h | --help` - Display a Help File

For Multiple Operations: There are a few separate blocks that are supported...

`[<Key> -w <New Value>]`

`[-d <Key>]`

`[-v <Key>]`
