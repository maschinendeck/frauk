## frauk
### matekasse & more

[Mete](https://github.com/chaosdorf/mete) Clone based on Python and Flask.

#### Import from [Mete](https://github.com/chaosdorf/mete)

The import only works if no frauk db exists.

    $ mv app/dev.db app/dev.db_bak
    $ python mete_import.py /path/to/mete_database.db

That's it.

#### Roadmap
* zunächst als [Mete](https://github.com/chaosdorf/mete) Clone mit Python und Flask [95%]
* Admin Panel zum Editieren von Usern und Preisen.
* Barcode Scanner zum Scannen der Items
* User Auth über NFC Karten
* Getränkebestandsanzeige, Statistiken
* Gamification (Archivements oder so?)

