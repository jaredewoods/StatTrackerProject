FasdUAS 1.101.10   ��   ��    k             l    / ����  O     /  	  k    . 
 
     r        n    
    1    
��
�� 
time  4   �� 
�� 
docu  m    ����   o      ���� 0 currenttime currentTime      l   ��������  ��  ��        l   ��  ��    / ) Subtract 2 seconds from the current time     �   R   S u b t r a c t   2   s e c o n d s   f r o m   t h e   c u r r e n t   t i m e      l   ��  ��    * $ set adjustedTime to currentTime - 2     �   H   s e t   a d j u s t e d T i m e   t o   c u r r e n t T i m e   -   2      l   ��������  ��  ��       !   l   �� " #��   " 0 * Format the adjusted time into MMSS format    # � $ $ T   F o r m a t   t h e   a d j u s t e d   t i m e   i n t o   M M S S   f o r m a t !  % & % r     ' ( ' I   �� )��
�� .sysoexecTEXT���     TEXT ) b     * + * b     , - , m     . . � / / 
 e c h o   - o    ���� 0 currenttime currentTime + m     0 0 � 1 1 j   |   a w k   ' { p r i n t f ( " % 0 2 d % 0 2 d " ,   i n t ( $ 1 / 6 0 ) ,   i n t ( $ 1 % 6 0 ) ) } '��   ( o      ���� 0 formattedtime formattedTime &  2 3 2 l   ��������  ��  ��   3  4 5 4 l   �� 6 7��   6 3 - Copy the formatted timecode to the clipboard    7 � 8 8 Z   C o p y   t h e   f o r m a t t e d   t i m e c o d e   t o   t h e   c l i p b o a r d 5  9 : 9 I   "�� ;��
�� .sysoexecTEXT���     TEXT ; b     < = < b     > ? > m     @ @ � A A 
 e c h o   ? o    ���� 0 formattedtime formattedTime = m     B B � C C    |   p b c o p y��   :  D E D l  # #��������  ��  ��   E  F G F l  # #�� H I��   H !  Pause the QuickTime Player    I � J J 6   P a u s e   t h e   Q u i c k T i m e   P l a y e r G  K L K I  # +�� M��
�� .MVWRpausnull���     docu M 4  # '�� N
�� 
docu N m   % &���� ��   L  O P O l  , ,��������  ��  ��   P  Q�� Q L   , . R R o   , -���� 0 formattedtime formattedTime��   	 m      S S�                                                                                  mgvr  alis    H  Main                           BD ����QuickTime Player.app                                           ����            ����  
 cu             Applications  +/:System:Applications:QuickTime Player.app/   *  Q u i c k T i m e   P l a y e r . a p p  
  M a i n  (System/Applications/QuickTime Player.app  / ��  ��  ��     T�� T l     ��������  ��  ��  ��       �� U V W X����   U ��������
�� .aevtoappnull  �   � ****�� 0 currenttime currentTime�� 0 formattedtime formattedTime��   V �� Y���� Z [��
�� .aevtoappnull  �   � **** Y k     / \ \  ����  ��  ��   Z   [  S������ . 0���� @ B��
�� 
docu
�� 
time�� 0 currenttime currentTime
�� .sysoexecTEXT���     TEXT�� 0 formattedtime formattedTime
�� .MVWRpausnull���     docu�� 0� ,*�k/�,E�O��%�%j E�O��%�%j O*�k/j 
O�U W @��J�J; X � ] ]  1 6 0 2��   ascr  ��ޭ