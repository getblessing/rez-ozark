
## Ozark

A production/development environment setup powered by [Rez](https://github.com/nerdvegas/rez), [Allzpark](https://github.com/mottosso/allzpark) and MongoDB.


![image](https://user-images.githubusercontent.com/3357009/90910495-fb4a2380-e409-11ea-9e92-0d004aeddd4c.png)


## Usage

Ozark ships with a MongoDB/[MontyDB](https://github.com/davidlatwe/montydb) based Rez package repository plugin which used to store Allzpark profile packages, you may see `ozark/config/rezconfig.py` for configuration details.

* Enter Ozark

    ```bash
    $ rez-env ozark
    ```

* Init profile at current working directory

    ```bash
    $ party --init
    ```

* Enable profile to MongoDB

    ```bash
    $ party --at release
    ```
    
* Or [MontyDB](https://github.com/davidlatwe/montydb)
    
    ```bash
    $ party --at install
    ```

* List out all profiles

    ```bash
    $ party --list
    ```
