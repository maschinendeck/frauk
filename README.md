![frauk](./logo.png)
## matekasse & more

A payment solution for our Hackspace inspired by
[Mete](https://github.com/chaosdorf/mete).
It's based on Python, Flask and GraphQL(graphene).
The WebApp will be based on ReactJS.

#### Import from [Mete](https://github.com/chaosdorf/mete)

The import only works if no frauk db exists.

    $ mv backend/dev.db backend/dev.db_bak
    $ python mete_import.py /path/to/mete_database.db

That's it.

#### Roadmap
* zunächst als [Mete](https://github.com/chaosdorf/mete) Clone mit Python und Flask [95%]
* Admin Panel zum Editieren von Usern und Preisen.
* Barcode Scanner zum Scannen der Items
* User Auth über NFC Karten
* Getränkebestandsanzeige, Statistiken
* Gamification (Archivements oder so?)
