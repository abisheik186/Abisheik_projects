import mysql.connector
from tabulate import tabulate
import inv_valid
try:
    mydb=mysql.connector.connect(
        host='localhost',
        user='root',
        password='Abisheik@12',
        database='abisheik'
        )
    cur=mydb.cursor()
    class Inventory:
        def user_input(self):
            while True:
                pr_name=input('Enter product name :')
                if inv_valid.prod_valid(pr_name):
                    break
            while True:
                quantity=float(input('Enter product quantity :'))
                if inv_valid.valid_quantity(quantity):
                    break
            while True:
                pr_price=input('Enter unit price :')
                if inv_valid.prod_price_valid(pr_price):
                    break
            while True:
                supplier_name=input('Enter product supplier name :')
                if inv_valid.name_validation(supplier_name):
                    break
            cur.execute('select prod_name,supplier_name from inventory')
            det=cur.fetchall()
            a=(pr_name,supplier_name)
            if a in det:
                query=('update inventory set quantity=quantity+%s where prod_name=%s and supplier_name=%s')
                values=(quantity,pr_name,supplier_name)
                cur.execute(query,values)
                mydb.commit()
            else:
                query=('insert into inventory(prod_name,quantity,unit_price,supplier_name) values(%s,%s,%s,%s)')
                values=(pr_name,quantity,pr_price,supplier_name)
                cur.execute(query,values)
                mydb.commit()
            print('product stored in database successfully')
        def display(self):
            cur.execute('select * from inventory')
            headers=['product ID','product name','quantity','unit price','supplier name']
            print(tabulate(cur.fetchall(),headers=headers,tablefmt='grid'))
        def update(self):
            cur.execute('select * from inventory')
            table_val=cur.fetchall()
            b=False
            while True:
                u_id=int(input('Enter product id to update :'))
                for i in table_val:
                    if u_id in i:
                        b=True
                        break
                if b==True:
                    break
                else:
                    print("Invalid ID ! !!")
            (cur.execute(f'select * from inventory where prod_id={u_id}'))
            print(cur.fetchall())
            lis_col=['prod_name','quantity','unit_price','supplier_name']
            print('1.product name\n2.quantity\n3.unit price\n4.supplier name')
            while True:
                ch=int(input('which field do you want to update :'))
                if ch<(len(lis_col)+1):
                    break
                else:
                    print('please enter valid choice')
            val=input('enter new value :')
            print(f'{lis_col[ch-1]} updated succesfully')
            query=(f'update inventory set {lis_col[ch-1]}=%s where prod_id=%s')
            tup=(val,u_id)
            cur.execute(query,tup)
            mydb.commit()
        def delete(self):
            cur.execute('select * from inventory')
            table_val=cur.fetchall()
            b=False
            while True:
                while True:
                    d_id=input('Enter product ID to delete :')
                    if inv_valid.id_valid(d_id):
                        break
                d_id=int(d_id)
                for i in table_val:
                    if d_id in i:
                        b=True
                        break
                if b==True:
                    break
                else:
                    print("Invalid ID ! !!")
            print(d_id)
            cur.execute('delete from inventory where prod_id={}'.format(d_id))
            mydb.commit()
            print('product record deleted successfully')
        def total(self):
            cur.execute('select * from inventory')
            col=cur.fetchall()
            lis_id=[]
            lis_prod=[]
            for i in col:
                lis_id.append(i[0])
                lis_prod.append(i[1])
            prod_tot_lis=[]
            cur.execute('select unit_price*quantity from inventory')
            for i in cur.fetchall():
                prod_tot_lis.append(int(i[0]))
            lis_tot=zip(lis_id,lis_prod,prod_tot_lis)
            print(tabulate(lis_tot,headers=['id','name','total'],tablefmt='grid'))
            print('Total inventory value :',sum(prod_tot_lis))
    s1=Inventory()
    def main():
        cur.execute('create table if not exists inventory\
    (prod_id int primary key auto_increment,\
    prod_name varchar(50) not null,\
    quantity float not null,\
    unit_price float not null,\
    supplier_name varchar(50) not null)')
        menu_dict={'1':s1.user_input,'2':s1.display,'3':s1.update,'4':s1.delete,'5':s1.total}
        while True:        
            print('1.Input product values\n2.view inventory records\n3.update existing records\n4.delete inventory record\n5.total inventory value\n6.Exit')
            ch=input('Enter choice :')
            if ch=='6':
                break
            else:
                if ch in menu_dict:
                   selec_opt=menu_dict[ch]
                   selec_opt()
                else:
                    print('invalid choice')

    main()
except Exception as e:
    inv_valid.log(e)
    print(e)
finally:
    cur.close()
    mydb.close()
    
