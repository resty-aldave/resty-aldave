import os


def folder_auto(path, index_name, start, end):
    for folder in range(start, end+1):
        
        folder_number = str(folder)
        
        full_name = os.path.join(path, index_name + folder_number)
        
        try:
            os.makedirs(full_name)
            print(f"✅ Created folder: {full_name}")
            
        except FileExistsError:
            print(f"⚠️ Folder already exists: {full_name}")
            
        except Exception as e:
            print(f"❌ An error occurred creating {full_name}: {e}")


folder_auto("/home/restyaldave/Desktop/School/SWU/College/S2Y1/PED 031", "PED 031_DAY ", 1, 15)
print("\nFolder creation process finished.")