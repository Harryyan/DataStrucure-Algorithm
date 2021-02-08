import java.io.UnsupportedEncodingException;
import java.nio.ByteBuffer;
import java.nio.CharBuffer;
import java.nio.charset.CharsetEncoder;
import java.nio.charset.StandardCharsets;
import java.util.Arrays;

// PROBLEM A valid UTF-8 string may contain only the following four bit patterns:

// 0xxxxxxx
// 110xxxxx 10xxxxxx
// 1110xxxx 10xxxxxx 10xxxxxx
// 11110xxx 10xxxxxx 10xxxxxx 10xxxxxx

// Write a function to determine whether a string meets this necessary (but not
// suf- ficient) criterion for UTF-8 validity.

public class ValidateUTF8 {
    public static void main(String[] args) {
        // String myString = "胜多负😺 World";
        // System.out.println(myString);
        // byte[] myBytes = null;

        // byte[] invalidUTF8Bytes1 = new byte[] { (byte) 0b10001111, (byte) 0b10111111
        // };
        // byte[] invalidUTF8Bytes2 = new byte[] { (byte) 0b10101010, (byte) 0b00111111
        // };
        // byte[] validUTF8Bytes1 = new byte[] { (byte) 0b11001111, (byte) 0b10111111 };
        // byte[] validUTF8Bytes2 = new byte[] { (byte) 0b11101111, (byte) 0b10101010,
        // (byte) 0b10111111 };

        // byte[] invalidBytes = new byte[] { (byte) 0b10001111, (byte) 0b10111111 };
        byte[] validUTF8Bytes1 = new byte[] { (byte) 0b11001111, (byte) 0b10111111 };
        final String converted = new String(validUTF8Bytes1, StandardCharsets.UTF_8);
        final byte[] outputBytes = converted.getBytes(StandardCharsets.UTF_8);

        System.out.println("#############");
        System.out.println(Arrays.equals(validUTF8Bytes1, outputBytes));

        // try {
        // myBytes = myString.getBytes("utf-32");
        // } catch (UnsupportedEncodingException e) {
        // e.printStackTrace();
        // System.exit(-1);
        // }

        // for (int i = 0; i < myBytes.length; i++) {
        // System.out.println(myBytes[i]);
        // }
    }

}

// ######## C language ############

// bool ValidateUTF8( const unsigned char* buffer, size_t len ) { int expected =
// 0; // Expected number of trailing bytes left for ( size_t i = 0; i < len; ++i
// ) {
// unsigned char b = buffer[i]; if ( IsTrailing( b ) ) {
// if ( expected-- > 0 ) continue;
// return false;
// } else if (expected > 0 ) {
// return false; }
// if ( IsLeading1( b ) ) { expected = 0;
// } else if ( IsLeading2( b ) expected = 1;
// } else if ( IsLeading3( b ) expected = 2;
// }else if(

// IsLeading4( b ) expected = 3;
// }else

// {
// return false;
// }
// }return(expected==0);}