import psycopg2 as db
import os

con = None
connected = None
cursor = None

def connect():
    global connected
    global con
    global cursor
    try:
        con = db.connect( 
            host = "localhost", 
            database = "mahasiswa", 
            port = 5432, 
            user = "ammar", 
            password = "2020"
        )
        cursor = con.cursor()
        connected = True
    except:
        connected = False
    return cursor

def disconnect():
    global connected
    global con
    global cursor
    if (connected==True):
        cursor.close()
        con.close()
    else:
        con = None
    connected = False
    print("PostgreSQL : Sambungan terputus")

def create_data():
    try:
        nim = input("Masukan NIM  : ")
        nama = input("Masukan Nama : ")
        idpro= input("Masukan ID Prodi : ")
        a = connect()
        sql = "insert into mahasiswa (nim, nama, idprodi) values ('"+nim+"', '"+nama+"', '"+idpro+"')"
        a.execute(sql)
        con.commit()
        print ("Data berhasil dibuat. \n")

    except(Exception, db.Error) as error:
        print ("Terjadi kesalahan memasukan data", error)

    finally:
        disconnect()

def read_data():
    try:
        a = connect()
        sql = "select * from mahasiswa"
        a.execute(sql)
        record = a.fetchall()
        
        for row in record:
            print("nim          = ", row[1])
            print("nama         = ", row[2])
            print("idprodi      = ", row[3], "\n")
        return record

    except(Exception, db.Error) as error:
        print ("Terjadi kesalahan menampilkan data", error)

    finally:
        disconnect()

def update_data():
    try:
        nim = input("Masukan NIM : ")
        a = connect()
        sql = "select * from mahasiswa where nim = '"+nim+"'"
        a.execute(sql)
        record = a.fetchall()
        print ("Data saat ini : ")
        
        for row in record:
            print("nim          = ", row[1])
            print("nama         = ", row[2])
            print("idprodi      = ", row[3], "\n")
        
        row = a.rowcount

        if(row==1):
            print ("Silahkan input untuk mengubah data...")
            nama = input("Masukan Nama Lengkap  : ")
            idprodi = input("Masukan ID Prodi     : ")
            a = connect()
            sql = "update mahasiswa set nama='"+nama+"', Idprodi='"+idprodi+"' where nim='"+nim+"'"
            a.execute(sql)
            con.commit()
            print ("Update data selesai. \n")
            
            sql = "select * from mahasiswa where nim = '"+nim+"'"
            a.execute(sql)
            rec = a.fetchall()
            print ("Data setelah diubah : ")
            
            for row in rec:
                print("nim          = ", row[1])
                print("nama         = ", row[2])
                print("Idprodi      = ", row[3], "\n")
            
            return record
            
        else:
            print ("Data tidak ditemukan. \n")

    except(Exception, db.Error) as error:
        print ("Terjadi kesalahan saat update data", error)

    finally:
        disconnect()
    
def delete_data():
    try:
        nim = input("Masukan NIM : ")
        a = connect()
        sql = "select * from mahasiswa where nim = '"+nim+"'"
        a.execute(sql)
        record = a.fetchall()
        print ("Data saat ini : ")
        
        for row in record:
            print("nim          = ", row[1])
            print("nama         = ", row[2])
            print("Idprodi      = ", row[3], "\n")
    
        row = a.rowcount

        if(row==1):
            jwb = input("Apakah anda ingin menghapus data ini? (y/t)")
            if(jwb.upper()=="Y"):
                a = connect()
                sql = "delete from mahasiswa where nim='"+nim+"'"
                a.execute(sql)
                con.commit()
                print ("Data berhasil dihapus. \n")
            else:
                print ("Data batal dihapus. \n")
        else:
            print ("Data tidak ditemukan. \n")

    except(Exception, db.Error) as error:
        print("Terjadi kesalahan saat menghapus data", error)

    finally:
        disconnect()
    
def search_data():
    try:
        nim = input("Masukan NIM : ")
        a = connect()
        sql = "select * from mahasiswa where nim = '"+nim+"'"
        a.execute(sql)
        record = a.fetchall()
        for row in record:
            print("nim          = ", row[1])
            print("nama         = ", row[2])
            print("Idprodi      = ", row[3], "\n")
    
        print ("Pencarian Selesai. \n")
        return record

    except(Exception, db.Error) as error:
        print("Terjadi kesalahan saat mencari data", error)

    finally:
        disconnect()


print ( " Nama : Ammar Abdurahman" )
print ( " Nim  : 200511127" )
print ( " Kelas: R1" )

def show_menu():
    print("\n APLIKASI DATABASE ")
    print("1. Insert Data")
    print("2. Show Data")
    print("3. Update Data")
    print("4. Delete Data")
    print("5. Search Data")
    print("0. Close")
    print("------------------")
    menu = input("Pilih menu> ")

    #clear screen
    os.system("cls")

    if menu == "1":
        create_data()
    elif menu == "2":
        read_data()
    elif menu == "3":
        update_data()
    elif menu == "4":
        delete_data()
    elif menu == "5":
        search_data()
    elif menu == "0":
        print ( " program selesai" )
        exit()
    else:
        print("Error, Pilih Ulang")

if __name__ == "__main__":
  while(True):
    show_menu()