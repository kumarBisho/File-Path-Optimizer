#include <bits/stdc++.h>
using namespace std;

vector<string> splitString(string A, char ch){
    vector<string> temp;
    
    A.push_back(ch);
    
    int n=A.length();
    string str = "";
    for(int i=0;i<n;i++){
        if(A[i]!='/'){
            str.push_back(A[i]);
        }else{
            if(str.length()!=0){
                temp.push_back(str);
            }
            str="";
        }
    }
    return temp;
}

string Solution::simplifyPath(string A) {
    vector<string> ans;
    
    string str=A;
    
    vector<string> temp = splitString(A, '/');
    
    for(int i=0;i<temp.size();i++){
        if(temp[i]=="." || temp[i]=="/") continue;
        else if(ans.size()!=0 && temp[i]==".."){
            ans.pop_back();
        }else if(temp[i]!=".."){
            ans.push_back(temp[i]);
        }
    }
    string result = "";
    
    if(ans.size()== 0) return "/";
    
    for(auto it: ans){
        result+="/" + it;
    }
    return result;
}

string input_string ;
cout<<"Enter the path: ";
cin>>input_string;

cout<<simplifyPath(input_string);