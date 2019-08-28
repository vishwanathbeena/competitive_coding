def findLongestSubstring(string):
    n = len(string)

    # starting point of current substring.
    st = 0

    # maximum length substring without
    # repeating characters.
    maxlen = 0

    # starting index of maximum
    # length substring.
    start = 0

    # Hash Map to store last occurrence
    # of each already visited character.
    pos = {}
    max_len={'length':0}

    # Last occurrence of first
    # character is index 0
    pos[string[0]] = 0

    start_list = []
    length_list = []
    sub_str_list = []

    for i in range(1, n):

        # If this character is not present in hash,
        # then this is first occurrence of this
        # character, store this in hash.
        
        if string[i] not in pos:
            pos[string[i]] = i

        else:
            # If this character is present in hash then
            # this character has previous occurrence,
            # check if that occurrence is before or after
            # starting point of current substring.
            if pos[string[i]] >= st:

                # find length of current substring and
                # update maxlen and start accordingly.
                currlen = i - st
                if maxlen < currlen:
                    maxlen = currlen
                    max_len['length'] = maxlen #setting maximum length in Dictionary to maxlen value
                    start = st
                    start_list.append(st)
                    length_list.append(currlen)
                else:
                    if maxlen ==  currlen :
                    #max_len['length'] = currlen
                     start_list.append(st)
                     length_list.append(currlen) 

                    # Next substring will start after the last
                # occurrence of current character to avoid
                # its repetition.
                st = pos[string[i]] + 1

            # Update last occurrence of
            # current character.
            pos[string[i]] = i

            # Compare length of last substring with maxlen
    # and update maxlen and start accordingly.
    if maxlen < i - st:
        maxlen = i - st
        start = st
        max_len['length'] = maxlen
    else:
     if maxlen == currlen:
        start_list.append(st)
        length_list.append(i - st )
        # The required longest substring without
    # repeating characters is from string[start]
    # to string[start+maxlen-1].
    for i in range(len(start_list)):
        if length_list[i] == max_len['length']:
          sub_str_list.append(string[start_list[i]:start_list[i]+length_list[i]])
    print(sub_str_list)
	
if __name__ == '__main__':
     string = "ABCDEFGOOABCDEFGHIJKOONPQRSTUVWXYZ"
     findLongestSubstring(string)
