def activation_key_manager():
    activation_key = input()
    while True:
        command = input()
        if command == "Generate":
            break
        
        parts = command.split(">>>")
        action = parts[0]
        
        if action == "Contains":
            substring = parts[1]
            if substring in activation_key:
                print(f"{activation_key} contains {substring}")
            else:
                print("Substring not found!")
        
        elif action == "Flip":
            case = parts[1]
            start_idx, end_idx = int(parts[2]), int(parts[3])
            if case == "Upper":
                activation_key = (activation_key[:start_idx] + activation_key[start_idx:end_idx].upper() +
                                  activation_key[end_idx:])
            else:
                activation_key = (activation_key[:start_idx] + activation_key[start_idx:end_idx].lower() +
                                  activation_key[end_idx:])
            print(activation_key)
        
        elif action == "Slice":
            start_idx, end_idx = int(parts[1]), int(parts[2])
            activation_key = activation_key[:start_idx] + activation_key[end_idx:]
            print(activation_key)
    
    print(f"Your activation key is: {activation_key}")

activation_key_manager()
