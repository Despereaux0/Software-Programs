import os
print ("Welcome to OCEAN SDN BHD Online Pharmacy Manadement System")

print("\n\n1.Admin\n2.New Customer\n3.Registered Customer\n")


choice=int(input (("Please Enter The Number of Who Are You:")))


if choice<=0 or choice>3 :
        print('Invalid input')

elif choice==1:
    print("\nYou Have Choosen, Admin ")

    adminpassword=(str(input("Please Enter The Given Admin Password:")))


    if adminpassword=="admin123":

        print("Login Successful!")

        print("\n\n1.Upload Medicine\n2.View all Uploaded Medicines\n3.Update Medicine Information\n4.Delete Medicine Information\n5.Search Medicine\n6.View Customer Orders\n7.Search Order of Specific Customer\n8.Exit")

        choice=int(input (("\nPlease Enter What Would You Like To Do:")))

        if choice<=0 or choice>8 :
                print('Invalid input')

        elif choice==1:


                mname=(input("Enter Medicine Name:"))
                mexd=(input("Enter Medicine Expiration Date:"))
                mp=(input("Enter Medicine Price:"))
                md=(input("Enter Medicine Description:"))

                addmedicine=open("txt1.txt","a")


                # addmedicine.write("\n")
                addmedicine.write(mname+",")
                addmedicine.write("Exp Duration:"+mexd+",")
                addmedicine.write("Price:"+mp+",")
                addmedicine.write("Specs:"+md+".")
                addmedicine.close()

                

        elif choice==2:

                viewmedicine = open("txt1.txt", "r")

                print(viewmedicine.read())
                viewmedicine.close()
                                        
         

        elif choice==3:
                data=open("txt1.txt",'r') 
                temp=open("temp.txt",'w') 
                mn=(input("Enter Medicine Name You Would Like To Change:")) 
                s=' '
                while(s):
                        s = data.readline()
                        L=s.split(",")
                        if len(s)>0:
                                if str(L[0])== mn:
                                        umname=(input("Enter New Medicine Name:"))
                                        umexd=(input("Enter New Medicine Experation Date:"))
                                        ump=(input("Enter New Medicine Price:"))
                                        umd=(input("Enter New Medicine Description:"))
                                        temp.write(umname+","+"Exp Duration:"+umexd+","+"Price:"+ump+","+"Specs:"+umd+"."+"\n" )
                                else:
                                        temp.write(s)
                temp.close()
                data.close()
                os.remove('txt1.txt')
                os.rename('temp.txt','txt1.txt')

                                     
        elif choice==4:
                data=open("txt1.txt",'r') 
                temp=open("temp.txt",'w') 
                mn=(input("Enter Medicine Name You Would Like To Delete:")) 
                s=' '
                while(s):
                        s = data.readline()
                        L=s.split(",")
                        if len(s)>0 and str(L[0])!= mn:
                                temp.write(s)
                temp.close()
                data.close()
                os.remove('txt1.txt')
                os.rename('temp.txt','txt1.txt')


        elif choice==5:


                searchmedicine = open("txt1.txt")


                seach_key = input('Enter the Uploaded Medicine You Want To Search: ')
                for line in searchmedicine:
                        if not seach_key in line :
                                continue

                        print(line)


        elif choice==6:

                print("Customer's Names and Orders")

                searchorder=open("order.txt","r")

                print(searchorder.read())
                searchorder.close()


        elif choice==7:

                
                
                search_order=open("order.txt")

                        
                search_name =(input("Enter the Name of The Customer:"))
                for line in search_order:
                        if not search_name in line : 
                                continue

                        print(line)


        elif choice==8:

                print("Thank You, Have a Great Day")



 

    else:
                print("Incorrect Password")



elif choice==2:

        print("\nYou Have Choosen, New Customer")


        print("\n\n1.View Medicine Details\n2.Register As A New Customer\n3.Exit\n")


        choice=int(input (("\nPlease Enter What Whould You Like To Do:")))


        if choice<=0 or choice>3 :
                print('Invalid input')


        elif choice==1:

            viewmedicine = open("txt1.txt", "r")
        
            print(viewmedicine.read())
            viewmedicine.close() 
    


        elif choice==2:

                    cname=(input("Please Enter Your Name:"))
                    cadd=(input("Please Enter Your Address:"))
                    cemail=(input("Please Enter Your Email:"))
                    cno=(input("Please Enter Your Contact No: "))
                    cgen=(input("Please Enter Your Gender(M/F/Other):"))
                    cdob=(input("Please Enter Date of Birth (DD/MM/YY):"))
                    
                        
                    addcli=open("cilentinfo.txt","a")

                    addcli.write("\n")
                    addcli.write(cname+", ")
                    addcli.write(cadd+", ")
                    addcli.write(cemail+", ")
                    addcli.write(cno+", ")
                    addcli.write(cgen+", ")
                    addcli.write(cdob)
                    addcli.close()

                    print("Thank You For Registering As a New Customer\nYour registered customer password is:customer123")



        elif choice==3:

                print("Thank You, Have a Great Day")




elif choice==3:

        print("\nYou Have Choosen, Registered Customer ")

        customerpassword=(str(input("Please Enter The Given Customer Password:")))


        if customerpassword=="customer123":

            print("Login Successful!")

            print("\n\n1.View Medicine Details\n2.Place Medicine Order\n3.View Own Order\n4.View Personal Information\n5.Exit")


            choice=int(input (("\nPlease Enter What Would You Like To Do:")))

            if choice<=0 or choice>5 :
                print('Invalid input')

            elif choice==1:


                viewmedicine = open("txt1.txt", "r")

                print(viewmedicine.read())
                viewmedicine.close()


            elif choice==2:


                    co=(input("Please Enter Your Name:"))
                    mo=(input("Enter Medicine Name You Would Like To Order(use , if more would like to be added):"))
                

                    addmedicine=open("order.txt","a")


                    addmedicine.write("\n")
                    addmedicine.write(co+" , ")
                    addmedicine.write(mo)
                    addmedicine.close()


            elif choice==3:


                search_order_name= open("order.txt")


                search_name =(input('Enter the Your Name:'))
                for line in search_order_name:
                        if not search_name in line : 
                               continue

                        print(line)



            elif choice==4:


                search_cilent_name= open("cilentinfo.txt")


                search_cilent =(input('Enter the Your Name:'))
                for line in search_cilent_name:
                        if not search_cilent in line : 
                               continue

                        print(line)





            elif choice==5:

                print("Thank You, Have a Great Day")


        else:

                print("Inccorect Password")

            
