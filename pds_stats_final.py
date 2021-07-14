#PDS Stats Final.ipynb



! pip install chart_studio
import requests 
import urllib.request
import plotly.graph_objects as go
 
import chart_studio
 
chart_studio.tools.set_credentials_file(username='Sleepyhead', api_key='ubG8jlRjLYavLW5jub2H')
 
import chart_studio.plotly as py
import chart_studio.tools as tls
 
################ FUNCTION TO INPUT VIDEO ID AND OUTPUT RESPONSE CODE AND VIEW COUNT
 
def  YT_API_pull(video_id):
  # open a connection to a URL using urllib
  webUrl ='https://www.googleapis.com/youtube/v3/videos?key=AIzaSyBInsFf7pyAxa1qEffe9CrSGNOcueNCqmw&fields=items(statistics(viewCount))&part=snippet,statistics&id=' + video_id 
  webUrl  = urllib.request.urlopen(webUrl)
 
  #get the result code and print it
  #print ("result code: " + str(webUrl.getcode()))
  rep_code = webUrl.getcode()
 
  # read the data from the URL and print it
  data = webUrl.read()
  #print (data)
 
  data = data.decode("utf-8")
 
  #By brute force, view count number in the response will start position: pos(viewCount) + 13
  #Better learn regex
  result = data.find('viewCount') 
  #print ("Substring 'viewCount ' found at index:", result ) 
 
  #output number
  num = ''
  i = result + 13
  while(data[i] != '"'):
    num = num + data[i]
    i += 1
 
  num = int(num)
 
 
  return rep_code, num
 
 
  ########## lect number and view count array
 
#Step 2 Add Video name to array
lect_no = ['V0', 'V1', 'V2 P1', 'V2 P2', 'V3 P1', 'V3 P2', 'V4', 'V5', 'V6', 'V7', 'V8', 'V9', 'V10', 'V11', 'V12', 'V13', 'V14', 'V15', 
'V16', 'V17', 'V18', 'V19', 'V20', 'V21', 'V22', 'V23', 'V24', 'V25', 'V26', 'V27', 'V28', 'V29', 'V30', 'V31a', 'V31b', 'V32', 'V33', 'V34', 'V35', 'V36']

#Step 3	Add  ############ YT_API_pull(video_id = 'video name')[1] ############## to this array
view_ct = [YT_API_pull(video_id = 'Bo7iVSs5z6s')[1], YT_API_pull(video_id = 'hYdZjXceBYg')[1], YT_API_pull(video_id = '3w-_NqFJW30')[1],
YT_API_pull(video_id = 'JYhUh_YYY9s')[1], YT_API_pull(video_id = 'uP7AI6rha9E')[1], YT_API_pull(video_id = 's_gEqgBbw9k')[1], 
YT_API_pull(video_id = 'iWEh8bqvseE')[1], YT_API_pull(video_id = '37RlofthNdM')[1], YT_API_pull(video_id = 'Phu6sGsK0g8')[1], 
YT_API_pull(video_id = 'iWrB-rhGAoo')[1], YT_API_pull(video_id = 'tuRYYn7ncZM')[1], YT_API_pull(video_id = 'zn18jg3B_CA')[1], 
YT_API_pull(video_id = 'bFMoUeXpFVg')[1], YT_API_pull(video_id = 'UK8BMltgpFI')[1], YT_API_pull(video_id = 'Ci_neJGO0gY')[1], 
YT_API_pull(video_id = 'rZbxPjyKbzE')[1], YT_API_pull(video_id = '504U7TOHSwA')[1], YT_API_pull(video_id = '0lIkg6AibMs')[1], 
YT_API_pull(video_id = '6DpoONQCt9g')[1], YT_API_pull(video_id = '_kmAOOWq4U8')[1], YT_API_pull(video_id = 'PKoQNxlTFnY')[1],
YT_API_pull(video_id = 'cxp_uGBDcaU')[1], YT_API_pull(video_id = 'ONFw_-NF1jg')[1], YT_API_pull(video_id = 'HQBmqCZyRUI')[1],
YT_API_pull(video_id = 'Siruz9slidg')[1], YT_API_pull(video_id = 'VA-e46Ze2ZE')[1], YT_API_pull(video_id = 'FdKyOyYpWHI')[1],
YT_API_pull(video_id = '1K0HZj0Yyhw')[1], YT_API_pull(video_id = '-eUfWhpwBr0')[1], YT_API_pull(video_id = 'HrU7Gbc7FVk')[1],
YT_API_pull(video_id = 'PLrAiFOtIng')[1], YT_API_pull(video_id = '4Xa5C8E_8iM')[1], YT_API_pull(video_id = 'qDoilKqIAHU')[1], 
YT_API_pull(video_id = '4XQqfv-i5lk')[1], YT_API_pull(video_id = 'nwYXFfaS9NM')[1], YT_API_pull(video_id = 'ON2yxzKOXTU')[1],
YT_API_pull(video_id = 'bN4Cv4htq0g')[1], YT_API_pull(video_id = '6YKS-EgaaHQ')[1], YT_API_pull(video_id = 'jnHXbcXW-Xk')[1], 
YT_API_pull(video_id = 'A-4CmLeYntc')[1]]
 
 
 
# print(lect_no)
# print(view_ct)
 
##########    PLOTLY GRAPH RENDER
fig = go.Figure([go.Bar(x=lect_no, y = view_ct)])
 
py.plot(fig, filename = "abc", auto_open = False)


'''

##########    PLOTLY GRAPH RENDER
fig = go.Figure([go.Bar(x=lect_no, y = view_ct)])
fig.show()

##########    PLOTLY GRAPH RENDER
fig = go.Figure([go.Bar(x=lect_no, y = view_ct)])
fig.show()
fig.write_html("/content/file.html")

##########    PLOTLY GRAPH RENDER
fig = go.Figure([go.Bar(x=lect_no, y = view_ct)])
fig.show()
fig.write_html("/content/file.html")

'''
