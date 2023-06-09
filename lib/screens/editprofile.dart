import 'dart:convert';

import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import 'package:vehicle_rental/constants.dart';
import 'package:vehicle_rental/providers/accountprovider.dart';

import 'package:http/http.dart' as http;
import '../env.dart';
import '../models/account.dart';
import 'homepage.dart';

class EditProfile extends StatelessWidget {
  const EditProfile({super.key});

  Future<void> showFailure(BuildContext context) async {
    return showDialog(
        context: context,
        builder: ((context) {
          return AlertDialog(
            title: const Text(
              "Error",
              style: TextStyle(
                fontWeight: FontWeight.bold,
                fontSize: 25,
                color: Colors.red,
              ),
            ),
            content: const Text("Failed to edit.",
                style: TextStyle(
                  fontSize: 15,
                  fontWeight: FontWeight.bold,
                  color: textColor,
                )),
            actions: [
              TextButton(
                onPressed: () {
                  Navigator.pop(context);
                },
                child: const Text("OK"),
              )
            ],
          );
        }));
  }

  @override
  Widget build(BuildContext context) {
    TextEditingController userNameEditor = TextEditingController();
    TextEditingController firstNameEditor = TextEditingController();
    TextEditingController lastNameEditor = TextEditingController();
    userNameEditor.text = context.read<AccountProvider>().username!;
    firstNameEditor.text = context.read<AccountProvider>().firstName!;
    lastNameEditor.text = context.read<AccountProvider>().lastName!;
    return Scaffold(
      backgroundColor: bgColor,
      appBar: AppBar(
        centerTitle: true,
        title: const Text('Edit Account'),
      ),
      body: Column(
        crossAxisAlignment: CrossAxisAlignment.stretch,
        children: [
          const SizedBox(
            height: 20,
          ),
          Row(
            children: [
              const Text('Username:'),
              const SizedBox(
                width: 20,
              ),
              SizedBox(
                width: 200,
                child: TextField(
                  controller: userNameEditor,
                  decoration: const InputDecoration(
                      border: OutlineInputBorder(), labelText: 'Username'),
                ),
              ),
            ],
          ),
          const SizedBox(
            height: 20,
          ),
          Row(
            children: [
              const Text('First Name:'),
              const SizedBox(
                width: 20,
              ),
              SizedBox(
                width: 200,
                child: TextField(
                  controller: firstNameEditor,
                  decoration: const InputDecoration(
                      border: OutlineInputBorder(), labelText: 'First Name'),
                ),
              ),
            ],
          ),
          const SizedBox(
            height: 20,
          ),
          Row(
            children: [
              const Text('Last Name:'),
              const SizedBox(
                width: 20,
              ),
              SizedBox(
                width: 200,
                child: TextField(
                  controller: lastNameEditor,
                  decoration: const InputDecoration(
                      border: OutlineInputBorder(), labelText: 'Last Name'),
                ),
              ),
            ],
          ),
          ElevatedButton(
              onPressed: () {
                if (userNameEditor.text.isNotEmpty &&
                    firstNameEditor.text.isNotEmpty &&
                    lastNameEditor.text.isNotEmpty) {
                  Account old = context.read<AccountProvider>().acc!;
                  Account update = Account(
                      accountID: old.accountID,
                      username: userNameEditor.text,
                      password: old.password,
                      firstName: firstNameEditor.text,
                      lastName: lastNameEditor.text,
                      accountRole: old.accountRole,
                      isActive: old.isActive,
                      isStaff: old.isStaff,
                      isSuperuser: old.isSuperuser);
                  Map<String, String> headers = {
                    'Content-type': 'application/json',
                    'Accept': 'application/json',
                  };

                  String url = '${Env.prefix}/account/update/';

                  http.post(Uri.parse(url),
                      headers: headers, body: jsonEncode(update.toJson()));

                  context.read<AccountProvider>().setAccount(update);
                  Navigator.of(context)
                      .popUntil((route) => route.settings.name == '/');
                  Navigator.of(context).push(MaterialPageRoute(
                    builder: (context) => const HomePage(),
                  ));
                } else {
                  showFailure(context);
                }
              },
              child: const Text('Submit')),
        ],
      ),
    );
  }
}
